from enum import Enum


class State(Enum):
    PARIAL = "partial"
    COMPLETE = "COMPLETE"
    BLANK = "BLANK"

print(State.BLANK)
print(State("COMPLETE"))

for s in State:
    print(s)