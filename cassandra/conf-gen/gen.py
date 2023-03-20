import json
with open("conf.json") as f:
    p = json.load(f)
with open("conf.template.yaml") as f:
    t = str(f.read())
seeds = ":7000,".join(p)+":7000"
for addr in p:
    cfg = t.replace("$IP", addr).replace("$SEEDS", seeds)
    with open(f"./out/{addr}.yaml", "w") as of:
        of.write(cfg)