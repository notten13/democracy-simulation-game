# Democracy simulation game

This is a little Python game inspired by [Democracy 4](http://www.positech.co.uk/democracy4/).

After playing Democracy 4 I thought it would be an interesting challenge to try and recreate the basic components of the game. It's a good exercise to play with graphs, as every object simulated in the game is meant to be tightly connected to all the other ones.

The game allows the player to take the role of Prime Minister/President of a country and introduce new laws/update existing policies. Policies choices influence indicators (such as GDP, pollution levels, population health...) as well as voter happiness. The goal is to transform the country, while remaining popular enough to be re-elected.

## Get started

```
pip3 install -r requirements.txt
python3 main.py
```

## TODO

- [ ] Policy cost and income, and overall budget
- [ ] Voter group membership evolution
- [ ] Election logic
- [ ] Add a lot more policies and indicators
- [ ] Implement policy inertia
