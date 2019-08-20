Mary Ellen Carter Notes

## Pi
Not sure which model, but an old one. Has component video out.

On PCB:
Raspberry Pi
(c)2011.12

IP: 192.168.111.10

Startup script defined in `/etc/rc.local`
(currently `/home/pi/pixelpusher/FullCycle.py`)

## Access Point

IP: `192.168.1.5`
SSID: `Mary Ellen Carter`

Plug into switch from 1 of the 4 *LAN* ports, **not** the WAN port.

## LED Strips

The precut silicone old ones we have (28 working as of 2018, stored in black screw-top PVC tube in Reno as of 2019) are APA102. Apprently we bought them directly from Illumn back in the early days.

Various other strips added in 2019. I am working on detecting their various schema.

## Vehicle

2006 Dodge Durango
VIN: `1D8HD48N44F150146`

## People

### Tom Hallaran  (415) 866-9963
### Dan Beckmann  (415) 912-6625

### Tom Kim       (313) 420-7303
Burning Man art car veteran, has worked on a few and joined Three Mile Rock in 2019.

### Wes Huelskamp (910) 650-6169
Reno mobile mechanic Tom found, is willing to work on art cars and is pretty cheap.

### Alex Simone   
Hobby race car mechanic, has been to Burning Man, came out in July 2019 to diagnose car issues.

## Lore

The car was built by Decadent Oasis.
Three Mile Rock bought it in 2015/2016?

Search Jacob's email from Gilbert for some good detail on the purchase.

## Assorted Chat/Email Transcripts

### 8/8/2019 – 8/9/2019

Tom Hallaran:
  Hey Wes - looping you in to the crew working on the car! Definitely someone in this group can answer some questions...
Alex Simone:
  Hey Wes this is Alex. I was out in Reno working with Tom on the car last weekend. Feel free to call or text with questions. I am Detroit based so I'm on Eastern time.
Wes Huelskamp:
  Wondering how you determined it has no spark or injector pulse?
Alex Simone:
  Honestly I am a bit unsure about spark, we did a visual test with the spark/coil pulled from cyl 1 and saw no arc, but it is sunny in Reno after all. For the injector pulse I put a noid light on cyl 8 injector and observed during the crank event...
Tom Hallaran:
  Pretty sure about spark 
Alex Simone:
  One fluke time when I had the light installed, it did light up, and during that particular crank event the engine started without any need for starter fluid
  Every other time the light was dark and the engine only cranked
  I wrote up a couple of summary emails that include some feedback I got from the garage techs where I work (including our product electronics guy). Happy to forward that info along if nobody else has yet.
Wes Huelskamp:
  Just curious because starting fluid is not going to magically make the injectors and coils work. I think its probably coincidence. 
  I think I just need to check it out for myself. Is the battery still charged up?
Tom Hallaran:
  Yeah battery is good
  But charger is removed
  Need to install the new one
  Hey Wes also the Haines manual for the Durango is in the big husky toolbox next to the fence...
Wes Huelskamp:
  Alright
  Im about to go get a starter for you. How do you know its been running hot? Where is the temp gauge?
Tom Hallaran:
  No temp gauge , it just quits out on the playa
  But more during the day 
Wes Huelskamp:
  Then it starts right back up? Or you have to wait awhile?
Tom Hallaran:
  We gotta wait
Wes Huelskamp:
  Dies randomly, no spark and no injector pulse - sounds more like a crankshaft position sensor issue. If the computer gets no signal from that sensor it won't be able to pulse injectors or fire plugs. Just a shot in the dark at this point since the data link connector doesn't work and I can't see any live data or trouble codes. I think I need to figure out how to get that working before anything. 
  Then you would be able to see the temperature via a scan tool as well. 
  Let me know if you want me to do that and I'll get going on it. 
Tom Hallaran:
  Sounds like a good plan
  I think the junction box under the chassis could be an issue
Wes Huelskamp:
  👍
Tom Hallaran:
  The engine is under carpet as well as under that wood cover, lots of r value
Wes Huelskamp:
  Looks like you're correct. All the communication circuits run through one of those smaller connectors on that junction block. There's no signal on a couple of the circuits. We are going to need a new junction block before I can go any further. I can get the starter installed in the meantime. 
Tom Hallaran:
  Awesome - hopefully I am . Give me an address and I'll ship to you
  eBay one is 60 dollars 
  So I'd like to go with that V's the molar one
  Mopar one- is that good?
Wes Huelskamp:
  Yeah Mopar would be factory. Thats your best bet. 
  7235 Winterhill Ct. 
Reno, NV 89523
  I guess you already know, but make sure it looks like this:
  File Transfer: IMG_0335.jpg
Tom Hallaran:
  Yup that was my thought looks like shit
Dan Beckmann:
  🎉🎉
Jacob Ford:
  [images of engine and stuff]
Tom Hallaran:
  Wes got her starting so we should be able to move it forward to work on it this weekend! 
Alex Simone:
  Huzzah! Crank sensor did it?
  Or you mean with starter fluid and the new starter?
Wes Huelskamp:
  I started it around 15 times in the process of making sure it cranks every time with the key, so yes it definitely runs. Next step is to get the new junction block. Then I should be able to communicate with the computer and do proper diagnosis. 
Alex Simone:
  So was it the crank sensor?
Wes Huelskamp:
  I haven't replaced that yet. New starter today and had to figure out why it wouldn't start with the key, but did when I jumped power to the starter. 
  Once I can see all the live data from the sensors I will know more about the crank sensor. 
Alex Simone:
  Ok I see where you're at now, thanks


### 8/11/2019 – 8/16/2019

Tom Hallaran:
  Hey Wes jacob is trying to start the car with the key
  Is there something he needs to do?
Jacob Ford:
  File Transfer: IMG_2918.mov
Wes Huelskamp:
  Try holding the back of that connector tight while you crank it. There is a connection issue, which is why I’m going to wire in the starter switch. 
Jacob Ford:
  On it
  File Transfer: 58725752431__FB4A4574-B407-4B96-9555-02584061AA78.MOV
  Nice!
Tom Hallaran:
  As per Wes we should limit starting till he has push button working later this week
Wes Huelskamp:
  Got the oil changed, junction block installed, and the new starter switch wired in. It cranks consistently now, but decided it doesn’t want to start for me now. No spark or injector pulse. I back probed the crank sensor wires and verified it is sending a signal to the PCM, so that doesn’t seem to be the issue. All the injectors and coils have power, but its the PCM that directly controls them through a driver that grounds each one at a specific time. None of those control circuits are being grounded. Only thing I can figure is that the PCM is faulty 🤷🏼‍♂️
  File Transfer: IMG_0382.jpeg
  File Transfer: IMG_0383.jpeg
  $251.29 total for today.
Tom Hallaran:
  Uh oh
  Could the new block by faulty?
  What about the starter switch
  The green wire
  Maybe going through the relay is bad?
Wes Huelskamp:
  Made no difference with the old junction block. All the fuses in all the boxes are good. Wiggled tested all the wiring harnesses, still nothing. Not sure what happened between today and last week when I was here.
Tom Hallaran:
  Could it be battery?
  Could we try resetting ecm - take neg bat off - Turning key to on, leaving it for a while and putting key back on?
  Thanks for trying tonight
Wes Huelskamp:
  Already tried that multiple times. The battery is fully charged - don’t see that as a problem. 
Tom Hallaran:
  Ok will work on getting a new exam
  Ecm 
Wes Huelskamp:
  Sounds good. If you can send the payment for today to the same paypal that would be appreciated.
  Also I left the new junction block you bought in the box there in case you wanted to send it back.

### 8/16/2019 - 8/18/2019

Tom Hallaran:
  Creating a text chain here re the art Car
  Tom Kim will be on site, seems like we ran into a problem today
Tom Kim:
  What's going on
Tom Hallaran:
  File Transfer: IMG_2548.jpg
  Sharing for awareness
Tom Kim:
  I could be the imobilizer If youre jumping the ignition key tumbler, there's a chip that needs to tell the immobilizer to give the signal to start and ground the coils 
Tom Hallaran:
  The SKIM module was removed
  It's not there (chip) - but if the pcm thinks it needs skim then I think the failure mode looks like this... 
  But we have no code reading ability so it's hard to verify anything 
Tom Kim:
  I think I'm here 
  File Transfer: IMG_20190817_113727_01.jpg
  Is this the spot?
Tom Hallaran:
  Yes
  Back lot
  https://www.garretttuning.com/products/chrysler-jeep-dodge-ecm-pcm-security-removal-skim-delete-programming
  That guy for example will take the skim off a pcm for $
  Maybe we can find a local service?
Tom Kim:
  gates lockd w chain around it 
Jacob Ford:
  Mailbox says Wright on it. Hide-a-key for gate lock is inside lawn mower under hood.
Tom Kim:
  File Transfer: IMG_20190817_114024_01.jpg
Jacob Ford:
  Yep. You in? Make sure key goes back there.
Tom Kim:
  File Transfer: IMG_20190817_120224_01.jpg
  Was this ecu replaced? 
  File Transfer: _20190817_121224.jpg
  I can't connect to it it's locked out. Where did this come from? Is the original key, dashboard, ecu around?
Tom Hallaran:
  Yes it was
  Junkyard  2 years ago
  You could try that
   Ode reader doesn't work we have not really tried cleaning it
  Code 
  Cleaning the port
Tom Kim:
  Did it work after replaced? This doesn't look like the original key if it's a 2006
Tom Hallaran:
  Yes it worked
  The skim module which does the key vin ecm handshake is also gone 
  There is no vin coded in the pcm
Jacob Ford:
  File Transfer: IMG_2920.MOV.3gp
Tom Hallaran:
  Which probably means it should not work after some set of starts amount other things
Tom Kim:
  Did it come with a matching key? Obd can't get in because of immobilizer
Tom Hallaran:
  No that's gone
  But also
  The SKIM module is gone that would even 'read ' the key
  This guy can remove skim from a pcm/ecm and is in Ohio
  https://www.garretttuning.com
  Maybe we can find someone local?
  It was starting with key and some shorted wires 3 days ago, then some wiring happened and then This
Tom Kim:
  Was the immobilizer removed to start?
  Which 3 wires?
Tom Hallaran:
  The SKIM unit was removed during same year as engine swap 
  The immobilizer is also part of pcm though
  Pcm is what dodge calls ecm/Ecuador in this car
Tom Kim:
  It's started 3 days ago without the aid of starting fluid? Im wondering how it even ran without the immobilizer 
Tom Hallaran:
  I'm not sure odb won't work at all in immobilizer engine
  http://www.obd2.com/support/reprog/downloads/chrysler/chry-skim_initial.pdf
  Immobilized will ask the dodge tuning /skim removal guy if he calls back
  It started for 3 years
  But our OBd has never worked
Tom Kim:
  So how does the ecu get signal to fire? If it's missing, it was bypassed we should dig deeper instead of getting a new one flashed 
  No even worried about obd we past that 
Tom Hallaran:
   Without a code reader this is really painful
  Yeah cool we'll the issue is the pcm now
  Well
  According to Wes who did the most recent work and is on this chain
  Ignition goes to pcm
  It's getting correct voltage from key assembly switch
  All coils and plugs etc are powered
  And pcm isn't grounding them like it should
  There is no spark/ no injector pulse - seems immobilized 
  This happened before
  And is why we swapped out the pcm 2 years ago
  Yesterday Wes tried installing a new junction block and put in the push button start
  You should be able to crank it now
  But I have not seen this personally
  But yeah - now starting using the turn key and squeeze wires method jacob sent in that video doesn't work 
Tom Kim:
  Ecu doesn't usually go bad its the last resort crank switch is useless when the ignition switch already hits the contactor for the starter. Idk why the bypass is nece6
  Necessary
  I'll do some poking around I have the manual and I'll look at the skid for ignition and security
Tom Hallaran:
  Ok. Just to restate we - don't have a vin, a pcm coded to vin, or the skim key reader immobilized component or a key with a chip in it 
  Good luck - let us know if there is anything we can do to help
Wes Huelskamp:
  The key would not crank the starter without holding the connector very specifically on the back of the ignition switch. If I wiggled and/or put pressure on the back of the ignition switch connector sometimes it would crank, and sometimes it wouldn't. This is why I installed the push button switch for the starter to bypass the ignition switch that was not working consistently. 
Tom Kim:
  Did I ever start after the push to start?
  There's a green wire cut off of the back of the ignition with a butt splice 
  File Transfer: IMG_20190817_130901_01.jpg
Wes Huelskamp:
  Thats what used to be connected to the starter.  
Tom Kim:
  File Transfer: IMG_20190817_130950_01.jpg
  Is that this green wire for the starter¿
Wes Huelskamp:
  Yes
  You can try hooking it back into the ignition switch, but like I said it was giving me issues. 
Tom Kim:
  Gonna work on obd
  Try to*
Wes Huelskamp:
  What got it running?
Tom Kim:
  File Transfer: MOV_3883.mp4
  Sounds like a bad air leak
Tom Hallaran:
  Damn 👍 what did you do?
Wes Huelskamp:
  Yeah but what did you do to make it run?
  It wasn't firing at all for me. 
Tom Kim:
  The green starter wire to the ignition tumbler. Wheres the nearest jyard? 
  We should get a new one and connector and resplice every wire 
Wes Huelskamp:
  🤦🏼‍♂️
Tom Hallaran:
  Pick-n-Pull Cash For Junk Cars
2205 Larkin Cir, Sparks, NV 89431
(775) 359-4147
https://goo.gl/maps/EZgoKStBnRN2K6Ms6 had two Durangos but wes probably knows the best one
Tom Kim:
  That must have been their immobilizer bypass I didn't even get a chance to look at the electrical skid
Wes Huelskamp:
  That would be it Tom. Other places don't let you bring tools in and get your own stuff. 
Tom Kim:
  File Transfer: IMG_20190817_133053_01.jpg
  What's with this bus tho. Mechanical cat diesel 
Tom Hallaran:
  I don't get why the pcm isn't like 'we have security protocols ' but whatever glad it still works 
Wes Huelskamp:
  Yeah thats another burning man vehicle you might see there. Did some work on that bus too. 
Tom Hallaran:
  Dusty diesel 
Tom Kim:
  It's not turbo or heui but I like it, just like a tractor
  Actually is heui 
Dan Beckmann:
  https://www.hotwire.com/car-rentals/results/Reno%252C%2520NV%252C%2520United%2520States%2520(RNO-Reno-Tahoe%2520Intl.)/Reno%252C%2520NV%252C%2520United%2520States%2520(RNO-Reno-Tahoe%2520Intl.)/2019-08-17T14%253A00%253A00/2019-08-19T10%253A00%253A00
Tom Kim:
  How do y'all get power back here
Tom Hallaran:
  Run power from the back of the house in Front 
  With an extensión cord(s)
  Cords were In husky box 
Tom Kim:
  File Transfer: IMG_20190817_151423_01.jpg
  File Transfer: IMG_20190817_151423_02.jpg
  File Transfer: IMG_20190817_151423_03.jpg
  Harbor freight is having a 50 percent off at 3pm
  $275 3200w Jenny.
 $5 angle grinder lol 
  Also have solar panels and welders 
Dan Beckmann:
  Loved “Harbor freight is having a 50 percent off at 3pm”
  I have a generator 
  If you need to rent one 
Tom Kim:
  File Transfer: IMG_20190817_151735_01.jpg
  These are also handy cheapest way to light up a space
Dan Beckmann:
  Till we get there 
  That's cool 
Tom Kim:
  Just letting y'all know I'm coming back at 3 and getting angle grinder and this socket set for 20 bucks 
Dan Beckmann:
  Liked “Just letting y'all know I'm coming back at 3 and getting angle grinder and this socket set for 20 bucks ”
Tom Hallaran:
   I've!
  Metric open wrench set would be awesome if you can grab
Tom Kim:
  File Transfer: DSC_3884.jpg
  File Transfer: DSC_3885.jpg
Tom Hallaran:
  China is the best
Tom Kim:
  Do we have adrill ? 
  25 bucks
  Getting these things including the drill, didn't see one in the husky box 
Jacob Ford:
  Drill is at Dan's house but sure doesn't hurt to get a spare.
Tom Kim:
  It was cheap its a hammer drill too should be a little beefier 
Jacob Ford:
  AC or battery?
Tom Kim:
  Battery 
Tom Hallaran:
  Hows it going?
Tom Kim:
  File Transfer: DSC_3891.jpg
  Ignition switch isn't from a 2004-06 doesn match the jyardsdk gonna play sherlock
  Limitation
Jacob Ford:
  Yeah, we replaced that just last month. Old one has lost key.
Tom Kim:
  Don't need a key just the module behind it what car did y'all pull it from
Jacob Ford:
  That I'm not sure.
  I was pretty sure that was original but if you say it's not I believe you. Tom is that worth asking Gilbert?
  Also Tom Kim: we found the VIN! Let us know if helpful to you.
Tom Kim:
  File Transfer: IMG_20190818_160116_01.jpg
Tom Hallaran:
  File Transfer: IMG_2596.jpg
Tom Kim:
  Was not the original. Oem is made by  valeo  found it in a 2001 jeep
  6 digit of Vin is year cofe
  Code
  It's an 04 then not a 06. 01 Ignition switch doesn't have the imobilizer 
  This should work better. I was gonna map the pins with a multimeter and make a relay box but that would've taken a long minute 
Tom Hallaran:
  Awesome
  We only replaced the tumbler 
   Or the switch 
  Not the switch i mean
Tom Kim:
  File Transfer: IMG_20190818_160527_01.jpg
  Old vs new. We had a shitty aftermarket 
  Well I never buy Chrysler because they always grant the lowest bidder and change shit up in the middle of the same year
  File Transfer: DSC_3892.jpg
  International flatbed w. Split hubs. 
👁️♥️NV
  U guys got speakers on 3mr?
  Is there any starter spray?
  Hello?
Tom Hallaran:
  Their used to be spray around
        Yeah there are speaker we want to connect but we need a new car stereo/amp head
  Was 2 weeks ago
  Couple cans
Tom Kim:
  I could have got a new hu at the jyard I gotta track down the air leak, also the right bank valve cover is leaking and dripping slowly onto the header hence the smoke I'll grab a new set rn 
Tom Hallaran:
  Nice . Yeah we need a hu should be cheap at Walmart If we don't make it back to the yard
  Do you need spray to start?
Tom Kim:
  Spray to find the leal
  Leak
Tom Hallaran:
  Gotcha
  There were a couple cans for sure
  Maybe in a black tote
Dan Beckmann:
  Liked “International flatbed w. Split hubs. 
👁️♥️NV”
Tom Kim:
  File Transfer: DSC_3895.jpg
  All spliced up. Works great
Jacob Ford:
  Amazing!
Tom Hallaran:
  Loved an image
