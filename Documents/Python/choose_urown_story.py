from sys import exit
points = 0
hurt = 0
turtle = False
sword = True
def add_points():
    global points
    points += 1
def sub_points():
    global points
    points -= 1
def add_hurt():
    global hurt
    hurt += 1
def sub_hurt():
    global hurt
    hurt -= 1

def rock():
    print "It is a rather pecular large rock that seems to make feel like something is under the rock.  A bit confused and very curious, you press against the rock with all your might, straining against what feels like a mountain. You reach deep within youself and with every fiber of your body you will the boulder to move.  You even speak the word in your mind"
    choice = raw_input('> ')
    if "move" in choice:
        print "\nThe boulder, as if hearing your request, rolls away revealing a small hole. There is something back there. Awe struck you drag it out into the sunlight."
        sword()
        add_points()
    else:
        print "You are not yet strong enough to begin your journey."
        exit(0)

def sword():
     print "\nCaked with years of dust is a chest with your family's crest carved across the lid. The lock hanging from the front quickly taunts you to search for something to break it open. Finding a decent bashing stone you head over to the chest. Just as you raise the stone overhead the lock falls open. Opening the chest reveals an old sword and pair of battle sandles, both look as if they have seen some use, but you still don't know why they're here or to whom they belong. You hesitate as you reach in. Do you take them?"
     choice = raw_input('> ')
     if "yes" in choice:
         add_points()
         print "You told your mother about the sword and sandals, but she did not seem to want to tell you anything about them. You persisted and she finally broke down and told you the truth about your father's identity and that you must take the sword and sandals back to king Aegeus to claim your birthright."
         leave()
     else:
         print "You think better and put everything back as you found it. It's not yours after all. You head home not thinking too much of it. As dusk falls on the small town, a group of bandits slink into town and since there was only that one sword that you left in the fucking hole, everyone gets murdered."
         exit(0)

def leave():
    print "\nDo you want to believe this shit and \"follow your destiny?\""
    choice = raw_input('> ')
    if "yes" in choice:
        print "You decide to head out to find your father"
        path()
    else:
        sub_points()
        print "A group of bandits sneaking around the outskirts of town happen upon the boulder and opened chest. Putting the pieces together they realize something valuable must be nearby and track you back to the village. Seeing you turning in for the night, they wait until all is quiet then sneak in the house and kill your family before you fend them off."
        print "You look around at the blood, bodies, damage and loss and realize there is nothing here for you now. You grab your things and head out."
        path()

def path():
    print "\nLuckily you know an salty old sailor who makes routine trips to Athens delivering spices and textiles to the city. He actually owes you a favor. You know the sea is safe and the bandits prowl the road. How do you choose to travel?"
    choice = raw_input('> ')
    if "sea" in choice or "boat" in choice or "ship" in choice:
        sub_points()
        print "You start down to the docks and find Sipius. He was at his usual slip where you helped him load and unload his wares sometimes. Sipius welcomes you abord and settle in for the trip"
        meet_king()
    elif "land" in choice or "foot" in choice or "road" in choice:
        add_points()
        print "Emblazoned with a true sense of purpose you set off down the Traveler's Path."
        road()
    else:
        print "Not really knowing what to do next you slip into a nap...."
        path()

def road():
    print """\nIt's nice to be out on the road. The day seems to welcome you as your feet seem to chew up the miles. You stop at a creek for shade stop a cool drink. Might as well fill your               lambskin. Quite refreshed you get back on the path and as if out of nowhere you stumble upon obvious bandit with a big brass club. He shouts "I am Periphetes, the cudgel man, and I'm
    going to bash your head with this club."
    You only see 3 options:
    a) charge the bandit and whip his ass
    b) try to talk your way out of the fight
    c) turn back and take the ship
    """
    choice = raw_input('> ')
    if choice == "a":
        print "Your cunning and strengh far outmatches the brute Periphetes and you kill him. Standing over his broken body decide to take the club as a trophy to show off to anyone else in his crew."
        talk()
    elif choice == "b":
        add_points()
        print '"That\'s a mighty fine club you have there," You say. \n"Pure brass." He replied\n"I bet it isn\'t." \n"Yes it is." \n"It\'s just wood wrapped in brass." \n"Here, look at it to make sure." The idiot actually handed you the club after which you proceded to knock the shit out of him. You stand over the broken man weilding his own club. "You\'re right. This thing is solid brass. I think I\'ll keep it. Thanks Perry!"'
        talk()
    elif choice == "c":
        sub_points()
        print "You decide to the danger is too great and head back to the harbour"
        path()
    else:
        print "not an option"
        road()

def talk():
    print """'That was fun' you muse continuing down the path up to the cliffs. You smiled recounting the campfire story about a nutso man-eating turtle that lived the cliffs and it made you hate turtles growing up. "Oi!" The shout was defening, nearly causing you to loose your footing, you were so lost in that stupid turtle story. Casting you eyes upward you see him. A giant leaning on a battle axe lookin all sorts of nasty. "I am Sciron and these are my cliffs. To pass you must wash my feet as a toll!" he said. \n"What would happen if I didn't?" you replied. "I will chop off your head with this axe, and don't think that puny little twig you're carrying will save you, you're absolutely...WRONG!!!!" Sciron yelled. So you decide...
    a) You gonna fuck. this. giant. up.
    b) It's a dumb giant. Use your words.
    c) Wash his feet. Try not to get eaten.
    d) Nope. Get the ship. Get the fucking ship.
    """
    choice = raw_input('> ')
    if choice == 'a':
        sub_points()
        add_hurt()
        print "\nIts a fucking giant homie. What do you think happened. He flicked you over the ledge where you get to meet Bubbles, the dumb giant's giant man-eating turtle"
        turtle()
    elif choice == 'b':
        sub_points()
        print "\nYou know there is no way he'll win this battle of wits, however your smile instantly fades when he grabs you and chucks you over the ledge where you get to meet Bubbles, the dumb giant's giant man-eating turtle"
        turtle()
    elif choice == 'c':
        add_points()
        global turtle
        turtle = True
        print "You have scrubbed the shit outta that stable countless times. 'This is just like that. I'm just scrubbin horse shit just like last week.' You start in washin his feet and climb over one of them to get to the other side. Thats's when you see it. 'Is that a giant fucking turtle?' Sciron peers over the ledge and smiles, 'Sure is little man.' Holy shit Batman! He's the turtle guy! How did that story go? You can't remember but you're pretty sure it doesn'e end well for anyone scrubbing his feet. He lifts a foot and you seize the opportunity quickly snapping the handle to the brush and running into the sole of his foot. 'AAAHHHH!' he booms as you grab him by the tetering ankle and with the power of a god, you whip him over the cliff where hopefully the turtle will handle him."
        wash()
    elif choice == 'd':
        sub_points()
        print "You decide the danger is too great and head back to the harbour"
        path()
    else:
        print "not an option"
        talk()

def turtle():
    print "As you tumble down the mountain you hear the giant laughing 'You'll be a tasty one for Clyde!' You land on the beach and stare up at your childhood nightmare, a twenty foot tall pissed off hungry lookin man-eating turtle, who was licking his beak and staring at you. Really glad I found this sword. Alright he's a turtle so as long as I move quickly.. \nAttack high or low?"
    choice = raw_input('> ')
    if choice == 'high':
        print "You dash to the left and leap on a boulder propeling yourself like a missle towards the beast's head. Faster than you thought he turns snapping his jaws inches from your leg. As you roll to the ground he lunges again, now you have the beast timed and you expertly dodge to the side and slice open his neck."
        sub_hurt()
        wash()
    elif choice == 'low':
        print "You break out in a full sprint directly for the beast and dart to the left as he lunges, running your blade across the inside of his leg. You quickly dive to the next one and open up the tendon, bringing the beast to his knees, nearly crushing you in the process. You glance up at the giant fuming, as you land the finishing blow."
        sub_hurt()
        wash()
    else:
        turtle()

def wash():
    print """\nAs you climb back to the path out of the cliffs, you hope the weird shit is over with. You didn't think this was the kind of trouble you were going to find on the road. The path is settling out now and a gentle forest has begun framing trail. Up ahead you see a strange sight. Some guy holding a bent over tree. "I need your help" cries out. "I can't keep holding this tree."
    What a day...
    a) Sorry old man I got shit to do
    b) I could use an easy notch in my belt, I'm snuffin you out old man
    c) It's just an old man holding a tree bent over in the middle of the road. Sure I'll help him out.
    """
    choice = raw_input('> ')
    if choice == 'a':
        print "You pass by the old man who admitidly looked a little mad. As soon as he is behind you THWACK! and the light fades out. You wake up in a ditch just outside Athens with no sword, no sandals, and no money."
        global sword
        sword = True
        global points
        points = 0
    elif choice == 'b':
        sub_points()
        add_hurt()
        print "You charge him and hurling the club at his head. To your astonishment the old man pulls some Yoda shit and catches the club and starts running at you. Usain Bolt couldn't have caught him. Weapons clash and parts of the forest are obliterated by the battle. He even landed a few good ones but, in the end was cut down like last years wheat."
        house()
    elif choice == 'c':
        add_points()
        print """"What do you need me to do?" you ask. \n"Just hold this tree top for me" he hands you the tree and you hold it, not really straining as much as you thought you would. The look on the old man's face was an odd mixture of anger and confusion. "Normally people will hold it and I let go and they go flyin but you aren't like the others. Are you a god. Cause you'd have to tell me if you were. Mortals aren't that strong." You didn't say anything mostly because you weren't sure about the whole god thing. He handed you another bent over tree "Just hold this one too." Something about his smile. You held tightly, but it was starting to pull you in opposite directions. The old man was only angry now "You have to be a god! Every mortal I have caught in this trap has been ripped clean in half!" \n"It must be these bitch ass trees you handed me old man. A child could hold these down. Here you try." No sooner had the pine-bender taken the trees than he relized he couldn't hold them and flashed you the oddest smile before he was ripped in half"""
        house()
    else:
        print "not an option"
        wash()

def house():
    print """You see a house.  This is the first hospitible looking anything you have seen in a while and it is getting dark.
    Do you
    a) see no reason to stop and continue on your way
    b) head up the walk and knock on the door
    """
    choice = raw_input('> ')
    if choice == 'a':
        meet_king()
    elif choice == 'b':
        justice ()
    else:
        print "not an option"
        house()

def justice():
    print """He knocked on the door. "My name is Procrustes. I have a magic bed for you to stay the night on. It is exactly six feet long, but can fit anyone, be they short or tall." Theseus had been warned about a man named Procrustes. His so called "magic" bed did fit anyone, but in an unpleasant way. If a person was too short, Procrustes would chain their arms and legs and stretch them. If they were too tall, he would chop off their legs until they were just right. Procrustes led Theseus into the room where the bed was."""
    print "Do you leave or decide to get some justice?"
    choice = raw_input('> ')
    if choice == "leave":
        sub_points()
        meet_king()
    else:
        add_points()
        print "Theseus pushed Procrustes onto the bed and chopped off his legs; and just so Procrustes wouldn't feel any pain, you sliced his head off too."
        meet_king()

def meet_king():
    print "It wasn't far from the house in the woods to the edge of the city of Athens. Theseus arrived and made his way to the palace to see the king Aegeus and his wife Madea. Many knew Madea was a sorceress and the king was under her spell, but the witch had made many powerful allies and knew her place was secure beside her king. She had read the bones knew Theseus would stir shit up so she convinced the king there was a man coming there to kill him and set up to poison him at dinner. He approached the palace. \"I\'d like to see the king.\""

def start():
    print """Pittheus, king of Troezen, who was famous for his wisdom and skill at expounding oracles. Pittheus understood the prophecy and introduced Aegeus to his daughter, Aethra, when Aegeus was drunk. But following the instructions of Athena in a dream, Aethra left the sleeping Aegeus and waded across to the island of Sphairia that lay close to Troezen's shore. There she poured a libation to Sphairos (Pelops' charioteer) and Poseidon, and was possessed by the sea god in the night. The mix gave Theseus a combination of divine as well as mortal characteristics in his nature; such double paternity, with one immortal and one mortal, was a familiar feature of other Greek heroes. After Aethra became pregnant, Aegeus decided to return to Athens. Before leaving, however, he buried his sandals and sword under a huge rock and told Aethra that when their son grew up, he should move the rock, if he were heroic enough, and take the tokens for himself as evidence of his royal parentage. In Athens, Aegeus was joined by Medea, who had left Corinth after slaughtering the children she had borne, and had taken Aegeus as her new consort. The Sorceress was gaining political favour while keeping the king and Athens under her spell. This brings us to you, Theseus. You were raised here in your mother's land. As you grew up and became a brave young man, you one day came across a rather large rock."""
    rock()


start()

locked_out = "The guard looks down at you and laughs. You can't get in to see king so you find a place to rest for the night. Madea's henchmen murder you in the night"
no_sword = "The celebration is open to all, but I doubt the king will see you. You get in the dining hall and make your way to the kings table. You announce yourself, but withot your family's sword the king doesn't recognize you. You wander back to your table defeated and have your last drink of wine."
two = "The celebration is open to all, but I doubt the king will see you. You get in the dining hall and make your way to the kings table. You announce yourself, but the king doesn't beleive you. 'You lie. You\'re naught but a mercenary sent to kill me. Guards! Off with his head!' Well, shit."
three = "The celebration is open to all, but I doubt the king will see you. You get in the dining hall and make your way to the kings table. You announce yourself. Seeing your sword and recognizing you as his son king Aegeus slaps the poisoned cup from your hand. The sorceress looses her shit and kills you and everyone in the kingdom."
four = "The celebration is open to all, but I doubt the king will see you. You get in the dining hall and make your way to the kings table. You announce yourself. Seeing your sword and recognizing you as his son king Aegeus slaps the poisoned cup from your hand. You and the king join together to battle sorceress but your injuries make it easy for her to trap in vial hanging from her neck where she was able to siphon off your life force to take over the kingdom as you watched nestled in her evil cleavage."
five = "The celebration is open to all, but I doubt the king will see you. You get in the dining hall and make your way to the kings table. You announce yourself. Seeing your sword and recognizing you as his son king Aegeus slaps the poisoned cup from your hand. You stand beside your father to battle the sorceress.  She tosses you aside and goes for the king.  Too injured from all you battles you cannot save your father. The evil bitch laughs at your loss as you drive your father's sword through her black heart.  With no ties to the throne any longer, you leave defeated, but still standing."
six = "The celebration is open to all, but I doubt the king will see you. You get in the dining hall and make your way to the kings table. You announce yourself. Seeing your sword and recognizing you as his son king Aegeus slaps the poisoned cup from your hand. You stand in front of your father, eager to end this bitch's life. You leap across the room as if in slow motion, and watch your blade slice through her neck, barely noticing her's slicing through your leg. The kingdom saved, you limp about the palace living out your days in quiet luxury."
seven = "The celebration is open to all, but I doubt the king will see you. You get in the dining hall and make your way to the kings table. Just before Theseus took a sip of the poisoned wine the king recognized his sword he left under a rock in the small town of Troezen and slapped the cup away. 'Guards! Arrest that bitch! She tried to murder the future king!' The two realized that as father and son they had a lot to catch up on and went on to fight many battles and live many adventures."

if sword == True:
    print no_sword
elif points == 0:
    print
elif points == 1:
    print locked_out
elif points == 2:
    print two
elif points == 3:
    print three
elif points == 4:
    print four
elif points == 5:
    print five
elif points == 6:
    print six
elif points >= 7:
    print seven
else:
    print "something broke"


print points
