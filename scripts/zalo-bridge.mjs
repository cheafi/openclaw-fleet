/**
 * Zalo Personal Account Bridge for OpenClaw
 * Uses zca-js (unofficial Zalo API) with QR code login
 *
 * First run: node zalo-bridge.mjs login
 *   → Shows QR code in terminal, scan with Zalo app
 *   → Saves session to ~/.openclaw/zalo-session/
 *
 * Then agents can use: node zalo-bridge.mjs <command> [args]
 */

import { Zalo, ThreadType } from "zca-js";
import fs from "node:fs";
import path from "node:path";

const SESSION_DIR = path.join(process.env.HOME, ".openclaw", "zalo-session");
const CREDENTIALS_FILE = path.join(SESSION_DIR, "credentials.json");
const CONTACTS_FILE = path.join(SESSION_DIR, "contacts.json");

fs.mkdirSync(SESSION_DIR, { recursive: true });

async function getApi() {
  const zalo = new Zalo();

  if (fs.existsSync(CREDENTIALS_FILE)) {
    const creds = JSON.parse(fs.readFileSync(CREDENTIALS_FILE, "utf-8"));
    const api = await zalo.login(creds);
    return api;
  }

  console.error("No session found. Run: node zalo-bridge.mjs login");
  process.exit(1);
}

async function login() {
  const zalo = new Zalo();
  console.log("Scan the QR code with your Zalo app...\n");
  const api = await zalo.loginQR();

  // Save credentials for reuse
  const creds = api.getContext().getCredentials();
  fs.writeFileSync(CREDENTIALS_FILE, JSON.stringify(creds, null, 2));
  console.log("\nLogin successful! Session saved.");
  console.log("You can now use zalo-bridge commands.");
  process.exit(0);
}

async function sendMessage(threadId, message, type = "User") {
  const api = await getApi();
  const threadType = type === "Group" ? ThreadType.Group : ThreadType.User;
  const result = await api.sendMessage({ msg: message }, threadId, threadType);
  console.log(JSON.stringify({ ok: true, messageId: result.msgId }));
}

async function sendBulkMessages(contactsJson, message) {
  const api = await getApi();
  const contacts = JSON.parse(contactsJson);
  const results = [];

  for (const contact of contacts) {
    try {
      await api.sendMessage({ msg: message }, contact.id, ThreadType.User);
      results.push({ id: contact.id, name: contact.name, status: "sent" });
      // Rate limit: 1 message per 2 seconds
      await new Promise((r) => setTimeout(r, 2000));
    } catch (e) {
      results.push({ id: contact.id, name: contact.name, status: "failed", error: e.message });
    }
  }

  console.log(JSON.stringify({ ok: true, results }));
}

async function findUser(phone) {
  const api = await getApi();
  const result = await api.findUser(phone);
  console.log(JSON.stringify(result));
}

async function createGroup(name, membersJson) {
  const api = await getApi();
  const members = JSON.parse(membersJson);
  const result = await api.createGroup({ name, members });
  console.log(JSON.stringify({ ok: true, groupId: result.groupId }));
}

async function addToGroup(groupId, memberId) {
  const api = await getApi();
  const result = await api.addUserToGroup(memberId, groupId);
  console.log(JSON.stringify({ ok: true, result }));
}

async function getGroupInfo(groupId) {
  const api = await getApi();
  const result = await api.getGroupInfo(groupId);
  console.log(JSON.stringify(result));
}

async function listFriends() {
  const api = await getApi();
  const result = await api.getFriendList();
  // Cache for agent use
  fs.writeFileSync(CONTACTS_FILE, JSON.stringify(result, null, 2));
  console.log(JSON.stringify({ count: result.length, friends: result.slice(0, 20) }));
}

// CLI
const [, , cmd, ...args] = process.argv;

switch (cmd) {
  case "login":
    await login();
    break;
  case "send":
    await sendMessage(args[0], args[1], args[2] || "User");
    break;
  case "send-bulk":
    await sendBulkMessages(args[0], args[1]);
    break;
  case "find":
    await findUser(args[0]);
    break;
  case "create-group":
    await createGroup(args[0], args[1]);
    break;
  case "add-to-group":
    await addToGroup(args[0], args[1]);
    break;
  case "group-info":
    await getGroupInfo(args[0]);
    break;
  case "friends":
    await listFriends();
    break;
  default:
    console.log(`Zalo Personal Bridge

Usage: node zalo-bridge.mjs <command> [args]

Commands:
  login                          Scan QR to login
  send <userId> <message> [type] Send message (type: User|Group)
  send-bulk <contactsJson> <msg> Send to multiple contacts
  find <phone>                   Find user by phone number
  create-group <name> <members>  Create group chat
  add-to-group <groupId> <uid>   Add user to group
  group-info <groupId>           Get group details
  friends                        List your friends`);
}
