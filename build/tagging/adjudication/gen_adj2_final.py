import json, os

BASE = os.path.expanduser("~/workspace/ap_world")

with open(f"{BASE}/build/cb-codes.json") as f:
    codes = json.load(f)
skill_defs = {s["code"]: s["skill"] for s in codes["skills"]}
topic_units = {t["code"]: t["unit"] for t in codes["topics"]}

with open(f"{BASE}/build/tagging/adjudication/ap_world-adj-2.json") as f:
    items = json.load(f)
item_by_id = {i["id"]: i for i in items}
assert len(items) == 25, len(items)

# (item_id, final_skill, final_topic, winner_skill, winner_topic, rationale, confidence)
D = [
 ("wh-fivesteps-u7-011", None, "7.4", None, "first",
  "Topic 7.4 (The Economy in the Interwar Period) wins: the stem asks what the 1939 chart conceals, and the answer is the 1932-33 collectivization famine - an interwar Soviet economic event, not 7.1's shifting-power thesis.",
  "high"),
 ("wh-fivesteps-u7-021", "2.A", None, "first", None,
  "Skill 2.A wins: the stem 'What psychological tactic is this?' asks the student to NAME the tactic (driving a wedge between soldiers and officers) - identifying the source's purpose, not explaining how it works. 2.B would require unpacking the POV/purpose, which the item does not demand.",
  "high"),
 ("wh-fivesteps-u8-003", "1.A", None, "recheck", None,
  "Skill 1.A wins: 'What was its most immediate human consequence?' is a single-answer identification of Partition's effect (15 million displaced). No explanation of how/why is required - the options are named outcomes.",
  "high"),
 ("wh-fivesteps-u8-013", None, "8.5", None, "recheck",
  "Topic 8.5 (Decolonization After 1900) wins: the item's core is the end of white minority rule via the 1994 ballot box - in the CB framework, white-minority-rule struggles sit under decolonization, not 8.7's global resistance movements.",
  "medium-high"),
 ("wh-fivesteps-u9-015", "1.A", None, "recheck", None,
  "Skill 1.A wins: 'What does a McDonald's in Shenzhen illustrate?' asks the student to identify the development the example exemplifies (global diffusion of standardized consumer culture), not to explain the process.",
  "high"),
 ("wh-fresh-u2-001", None, "2.5", None, "recheck",
  "Topic 2.5 (Cultural Consequences of Connectivity) wins: the answer identifies Battuta as a Muslim jurist judging Mali by Islamic legal/scholarly norms - the spread and normative force of Islamic culture across connected societies, not the 2.4 trade-route mechanics.",
  "medium-high"),
 ("wh-fresh-u3-021", None, "3.4", None, "first",
  "Topic 3.4 (Comparison in Land-Based Empires) wins: the stem 'most similar to which' is explicitly comparative - Qing vs Russian contiguous land-empire expansion. The comparison IS the assessed content.",
  "high"),
 ("wh-fresh-u4-006", None, "4.4", None, "recheck",
  "Topic 4.4 (Maritime Empires Established) wins: the VOC passage is about the mechanism of establishing empire (chartered 1602, forts, armies, treaties as a hybrid sovereign-company). It is not about maintaining/developing an established empire's economy (4.5).",
  "medium-high"),
 ("wh-fresh-u5-029", "1.A", None, "recheck", None,
  "Skill 1.A wins: 'This sequence best illustrates which broader pattern?' asks the student to identify the pattern the Hidalgo-to-Iturbide sequence exemplifies (elite capture of popular uprising), not to explain the mechanism.",
  "high"),
 ("wh-fresh-u5-039", None, "5.3", None, "recheck",
  "Topic 5.3 (Industrial Revolution Begins) wins: Watt's engine c.1780 is the canonical originating technology of the IR - location-independent rotary power that launched factory industrialization. 5.5 covers later Industrial-Age technology.",
  "high"),
 ("wh-fresh-u5-044", "6.C", None, "recheck", None,
  "Skill 6.C wins: the stem asks which argument the two excerpts TOGETHER best support. The student must reason about the relationship between the Declaration (1789) and the Napoleonic Code (1804) to evaluate the claim - using historical reasoning to relate pieces of evidence (6.C), not merely making a claim (6.A).",
  "medium-high"),
 ("wh-fresh-u5-054", "5.A", None, "first", None,
  "Skill 5.A wins: 'Comparing the outcomes... which statement is best supported?' The correct answer is a pattern statement (similar Enlightenment starts, sharply different outcomes). Identifying the pattern/connection across the two revolutions is 5.A; the item does not ask for the causal explanation of the difference (5.B).",
  "medium-high"),
 ("wh-fresh-u7-009", "5.A", "7.5", "first", "first",
  "Skill 5.A wins: 'differed most significantly from the Concert of Europe in that it' asks the student to identify the difference between two developments - a comparison, not an explanation of how one relates to the other. Topic 7.5 (Unresolved Tensions After World War I) wins: the League of Nations is the post-WWI settlement/international-order topic, not 7.1's power-shift thesis.",
  "medium-high"),
 ("wh-fresh-u8-002", "5.A", None, "first", None,
  "Skill 5.A wins: the stem literally asks 'which of the following connections' the two cases support - identifying the connection (varied paths within one decolonization wave). Not an explanation of how India relates to Ghana.",
  "high"),
 ("wh-fresh-u9-003", None, "9.5", None, "first",
  "Topic 9.5 (Calls for Reform and Responses) wins: the item is about Gorbachev's reforms (glasnost/perestroika) meant to preserve the system hastening its collapse - reforms and their outcomes, not 9.9's continuity-and-change framing.",
  "high"),
 ("wh-fresh-u9-013", "5.A", None, "recheck", None,
  "Skill 5.A wins: 'The report best illustrates the connection between communications technology and:' - identifying the connection (mobile phones enabling rapid protest organization beyond state media). 5.B would require explaining how one development relates to another, which the item does not ask.",
  "high"),
 ("wh-fresh-u9-023", None, "9.2", None, "first",
  "Topic 9.2 (Technological Advances and Disease) wins: the item is about AIDS activism campaigns expanding access to lower-cost antiretrovirals - disease and health, not 9.5 reform politics.",
  "high"),
 ("wh-princeton-pdf4-u6-011", "1.A", None, "recheck", None,
  "Skill 1.A wins: 'The irony of the cartoon depends on the viewer recognizing that' - identifying the historical concept (a nation of immigrants practicing racial exclusion). Pure identification.",
  "high"),
 ("wh-princeton-pdf4-u7-003", "1.A", None, "recheck", None,
  "Skill 1.A wins: 'reflects which of the following features of World War II' - identifying the feature (total-war mobilization of entire populations). Naming, not explaining.",
  "high"),
 ("wh-princeton-pdf4-u8-009", "1.A", None, "recheck", None,
  "Skill 1.A wins: 'belongs to which of the following broader twentieth-century developments' - identifying the broader development (anti-colonial movements for self-determination).",
  "high"),
 ("wh-princeton-pdf5-u2-001", "1.A", None, "recheck", None,
  "Skill 1.A wins: 'most directly illustrates which of the following' - identifying the development Musa's copper-for-gold account exemplifies (trans-Saharan trade).",
  "high"),
 ("wh-princeton-pdf5-u4-002", "1.A", None, "recheck", None,
  "Skill 1.A wins: 'most directly foreshadows which of the following' - identifying what Columbus's 'destitute of arms' description points to (Spanish arguments for easy conquest).",
  "high"),
 ("wh-princeton-pdf5-u4-012", "1.A", "4.4", "recheck", "first",
  "Skill 1.A wins: 'whose interests are most clearly ignored' - identifying the group (Indigenous peoples). Topic 4.4 (Maritime Empires Established) wins: the Treaty of Tordesillas dividing the world between Spain and Portugal is an act of establishing maritime empire, not the 4.2 exploration-causes framing.",
  "medium-high"),
 ("wh-princeton-pdf5-u6-005", "1.A", None, "recheck", None,
  "Skill 1.A wins: 'most directly demonstrates which of the following' - identifying the concept (Mughal symbolic authority as a focus of resistance).",
  "high"),
 ("wh-princeton-pdf6-u2-002", "1.A", None, "recheck", None,
  "Skill 1.A wins: 'best demonstrate about African trade networks' - identifying what interior-city prosperity shows (connection to long-distance caravan routes).",
  "high"),
]

# Validate decisions match disputed fields
final_arr = []
for iid, fs, ft, ws, wt, rationale, conf in D:
    item = item_by_id[iid]
    disputed = set(item["fields"].keys())
    entry = {"id": iid, "batch": item["batch"]}
    if "skill" in disputed:
        assert fs is not None, iid
        assert fs in skill_defs, f"skill code not verbatim: {fs}"
        assert skill_defs[fs] == item["skill_field"], f"parent skill mismatch {iid}: {fs}->{skill_defs[fs]} vs {item['skill_field']}"
        assert fs in (item["fields"]["skill"]["first"], item["fields"]["skill"]["recheck"]), f"skill pick not one of the reads: {iid}"
        entry["final_skill"] = fs
    else:
        assert fs is None, iid
    if "topic" in disputed:
        assert ft is not None, iid
        assert ft in topic_units, f"topic code not verbatim: {ft}"
        assert str(topic_units[ft]) == str(item["unit_period"]), f"unit mismatch {iid}"
        assert ft in (item["fields"]["topic"]["first"], item["fields"]["topic"]["recheck"]), f"topic pick not one of the reads: {iid}"
        entry["final_topic"] = ft
    else:
        assert ft is None, iid
    entry["decision_rationale"] = rationale
    entry["confidence"] = conf
    final_arr.append(entry)

# Count winners per field
from collections import Counter
c = Counter()
for _, _, _, ws, wt, _, _ in D:
    if ws: c[f"skill_{ws}"] += 1
    if wt: c[f"topic_{wt}"] += 1
print("field-level winners:", dict(c))

# 1. Write adjudication final JSON
out1 = f"{BASE}/build/tagging/adjudications/ap_world-adj-2-final.json"
with open(out1, "w") as f:
    json.dump(final_arr, f, indent=2)
with open(out1) as f:
    json.load(f)  # parse check
print("wrote", out1)

# 2. Append JSONL per batch
for iid, fs, ft, ws, wt, rationale, conf in D:
    item = item_by_id[iid]
    disputed = set(item["fields"].keys())
    wins = []
    if ws: wins.append(f"skill: third read sides with {ws} ({'first worker' if ws=='first' else 'rechecker'})")
    if wt: wins.append(f"topic: third read sides with {wt} ({'first worker' if wt=='first' else 'rechecker'})")
    line = {"item_id": iid, "final_skill": fs, "final_topic": ft,
            "worker": "thirdread-ap_world-adj-2",
            "note": "; ".join(wins) + ". " + rationale[:220]}
    path = f"{BASE}/build/tagging-audit/{item['batch']}-thirdread.jsonl"
    with open(path, "a") as f:
        f.write(json.dumps(line) + "\n")
print("jsonl appended per batch")

# Final cross-checks
assert len(final_arr) == 25
for e in final_arr:
    if "final_skill" in e:
        assert skill_defs[e["final_skill"]] == item_by_id[e["id"]]["skill_field"]
    if "final_topic" in e:
        assert str(topic_units[e["final_topic"]]) == str(item_by_id[e["id"]]["unit_period"])
print("ALL VALIDATION PASSED")
