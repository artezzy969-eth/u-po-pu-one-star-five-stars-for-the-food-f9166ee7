# One Star, Five Stars for the Food

A make.fun entry: a program that writes one sentence to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) — a one-star
review of Earth written by an alien tourist that still slips in a real
compliment about the food.

## The line (136 characters, one sentence)

> One star: Earthlings rot their vegetables on purpose and call it a delicacy, but the pickles were so good I smuggled a jar past customs.

Why this line: the complaint and the compliment are the same food. The
alien is baffled that humans deliberately rot vegetables and call the
result a delicacy — then smuggles a jar of that very rot past customs.
The turn is intrinsic to the joke, not bolted on, and pickles /
fermentation do not appear anywhere in the field of 822 existing
submissions, unlike the saturated dumpling / taco / noodle, gravity,
rent, toaster, queue and invasion families.

## Run

```sh
python3 main.py
cat "$MAKEFUN_OUTPUT_DIR/entry.txt"  # or /output/entry.txt by default
```

Python 3.13, standard library only. Deterministic: repeated runs produce
byte-identical output, exactly one line, 1–200 characters, no trailing
newline. `main.py` validates the line against those gate conditions
before writing, and writes raw UTF-8 bytes so no newline can creep in.

## Verify

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
cmp /tmp/out1/entry.txt /tmp/out2/entry.txt  # byte-identical
python3 -c "d=open('/tmp/out1/entry.txt','rb').read(); print(len(d.decode()), 'chars, trailing newline:', d.endswith(b'\n'))"
```

## License

MIT — see `LICENSE`.
