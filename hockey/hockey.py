import json
import random

defence = [1,2,3,4]
attack = [1,2,3,4]
pressure = [0,1,2,-2,-4,3]

def menu():
    print("""
    1.	Start Game
    2.	Edit Team
    3.	Create teams 
    4.	Match History / Leaderboard
    """)

    action = input("Choose what you want to do ")
    if action == "1":
        start()
    elif action == "2":
        edit()
    elif action == "3":
        team()
    elif action == "4":
        history()
names = []
with open('names.txt', 'r') as names:
    content = names.read().splitlines()
    names = content

team = []
with open('teamnames.txt', 'r') as team:
    content = team.read().splitlines()
    team = content
def display_history(hist):
    index = 0
    for x in range(len(hist['Results'])):
        print(hist['Results'][index])
        index = index + 1

def display_teams(team):
    index = 0
    for x in team:
        print(index, x['TeamName'])
        index = index + 1

def goalie(team):
    score = []
    for x in team:
        score.append(x["def"])
    return max(score)

def history():
    with open('result', 'r+') as f:
        data = json.load(f)
        display_history(data)

def result(team1,team1_score,team2,team2_score):
    with open ('result', 'r+') as f:
        data = json.load(f)
        data["Results"].append({team1:team1_score, team2: team2_score})
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def start():
    tempList = []
    player1_score = 0
    player2_score = 0
    player1 = []
    player2 = []
    with open('db', 'r+') as f:
        data = json.load(f)
        for x in data["Teams"]:
            tempList.append(x)
        try:
            display_teams(tempList)
            pl1 = int(input("Player1 choose team using index "))
            print("""
            

            """)
            display_teams(tempList)
            pl2 = int(input("Player2 choose team using index "))
            player1.append(data["Teams"][pl1])
            player2.append(data["Teams"][pl2])
            pl1_goalie = goalie(player1[0]["Players"])
            pl2_goalie = goalie(player2[0]["Players"])
        except:
            print("Invalid details have been provided")
            return
        for x in range(6):
            action = input("Player1: Type in shoot to take penalty ")
            if action == 'shoot':
                if pl2_goalie > player1[0]["Players"][x]["atck"] + random.choice(pressure):
                    print(player1[0]["Players"][x]["name"], "missed the penalty")
                else:
                    player1_score = player1_score + 1
                    print(player1[0]["Players"][x]["name"], "scored the penalty!")
            else:
                print("Missed")
                

        for x in range(6):
            action = input("Player2: Type in shoot to take penalty")
            if action == 'shoot':
                if pl1_goalie > player2[0]["Players"][x]["atck"]+ random.choice(pressure):
                    print(player1[0]["Players"][x]["name"], "missed the penalty")
                else:
                    player2_score = player2_score + 1
                    print(player1[0]["Players"][x]["name"], "scored the penalty!")
            else:
                print("Missed")
        if player1_score > player2_score:
            print("""
            player 1 wins
            """)
            print("player1 (",player1[0]["TeamName"],")", player1_score, "-"," player2 (", player2[0]["TeamName"], ")", player2_score)
            result(player1[0]["TeamName"],player1_score,player2[0]["TeamName"],player2_score)
        elif player1_score < player2_score:
            print("""
            player 2 wins
            """)
            print("player1 (",player1[0]["TeamName"],")", player1_score, "-"," player2 (", player2[0]["TeamName"], ")", player2_score)
            result(player1[0]["TeamName"],player1_score,player2[0]["TeamName"],player2_score)
        elif player2_score == player2_score:
            print("""
            Ended in a draw
            """)
            print("player1 (",player1[0]["TeamName"],")", player1_score, "-"," player2 (", player2[0]["TeamName"], ")", player2_score)
            result(player1[0]["TeamName"],player1_score,player2[0]["TeamName"],player2_score)
    menu()

def create_teams(no_of_teams):
    print(
        """
        WARNING!!! If team total score is more 
        than 35, the team will be deleted
        """
    )
    for x in range(no_of_teams):
        test = {"TeamName":random.choice(team),"id":x,"Players":[ 
            {"name":random.choice(names),"id":0,"def": random.choice(defence),"atck": random.choice(attack)},
            {"name":random.choice(names),"id":1,"def": random.choice(defence),"atck": random.choice(attack)},
            {"name":random.choice(names),"id":2,"def": random.choice(defence),"atck": random.choice(attack)},
            {"name":random.choice(names),"id":3,"def": random.choice(defence),"atck": random.choice(attack)},
            {"name":random.choice(names),"id":4,"def": random.choice(defence),"atck": random.choice(attack)},
            {"name":random.choice(names),"id":5,"def": random.choice(defence),"atck": random.choice(attack)}
            ]}
        with open('db','r+') as db:
            data = json.load(db)
            data["Teams"].append(test)
            db.seek(0)
            json.dump(data,db, indent=4)
    print("Teams created!")

def delete(team):
    with open('db', 'r+') as f:
        data = json.load(f)
        data["Teams"].pop(team)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def validate(player,team):
    atck = 0
    defence = 0
    with open('db', 'r+') as f:
        data = json.load(f)
    for x in range(6):
        atck = data["Teams"][team]["Players"][player]["atck"] + atck

    for x in range(6):
        defence = data["Teams"][team]["Players"][player]["def"] + defence
    
    total = atck + defence
    if total > 35:
        delete(team)

def edit():
    with open('db', 'r+') as f:
        data = json.load(f)
        print(data)
        team = int(input("Enter team id"))
        player = int(input("Enter player id"))
        attribute = input("Enter player attribute (def/atck)")
        value = int(input("Enter new Value"))
        try:
            if attribute == 'atck':
                data["Teams"][team]["Players"][player]["atck"] = value
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate() 
            elif attribute == 'def':
                data["Teams"][team]["Players"][player]["def"] = value
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
        except:
                print("Invalid data provided")
        validate(player,team)

menu()
