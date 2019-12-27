from typing import List


class Solution:
    def commonChars(self, a: List[str]) -> List[str]:
        mem = []
        for s in a:
            m = [0] * (ord('z') - ord('a') + 1)
            for c in s:
                m[ord(c) - ord('a')] += 1
            mem.append(m)

        common_chars = []

        for i in range(ord('z') - ord('a') + 1):
            if mem[0][i] > 0:
                common_chars.extend([chr(ord('a') + i)] * min(m[i] for m in mem))

        return common_chars


if __name__ == '__main__':
    import Test

    Test.test(Solution().commonChars, [
        ((["bella", "label", "roller"]), ["e", "l", "l"]),
        ((["cool", "lock", "cook"]), ["c", "o"]),
        ((["acabcddd", "bcbdbcbd", "baddbadb", "cbdddcac", "aacbcccd", "ccccddda", "cababaab", "addcaccd"]), []),
        (([
            "cxizlxaeicvxwiaqebzdzjfqmtjtrbnrehrisntpsmsntpsndsvjthgnubvekkxqwzknqqrcutenoeseqakkldnktsqpbhkklazy",
            "zohpatikncppgxcjpzazcwjaqbhuaokxabfvfrrbyvgjimfujzvsebjbvegwgapdixvzblrkqpzrdbtxlpultojuhwzqetvplpdf",
            "vutkluptjbjaahtaweadgtcvasaujlwgqrufojtakworsxlzlkkatwrnqxmtfbcmfjbbnpyitirnnvtmtlqxfzalycigeeeqtaqu",
            "intoasbpbflhukiroofoqzpeksolynoytjfbcmeoeamxxbnlfgdwjwpenhufllcrnjrxttbevqdxqmxyvvguuliqfvbdalpkbawy",
            "zizxutlyzcwwklwndwmgnquzfwaodungcpkhudujtfgcfpgsaatsflcxafskssjxhjhwexxgiwefozusudcxuwkroogopgcsjzgl",
            "lyesyttpoqgrplyxzpqqajqqafygvyuzkxwggpmpuvrlkgdzowyhhxjopcxtanieccgwzursvnvguwikgyszbybqthewgouzerpz",
            "msfudeekbpluzevvypmamrqhrdmjqclqsteprmpszzoigjuzrcofmtrasaokotykharcpddjufoufzoifrqlfpsfdemnptjxlaxv",
            "qcarngpdtsuakowbmkgnwmfjmjwmxkxeqpxyhcjnsrskuequgqlwppwwcgisepfnbxirpgynyymdqbzrbvmwupsvzdmylccylxkm",
            "opwvbicxbdcovfrlhxmqhytujlknkxazqooghibtajaojhssbbajzcqlyacbespfluawhygjwkfowcueylpogablbmmuhdkewhpv",
            "fuutvjfdwhhndlxuqxulutzepevejifzvkudvqqvkxhpkfixtrgugzyminanprvguibaocheuxqxhvxibyqjsomjdvnvxezmsorp",
            "myhbmytkraqvtvgygpmscwcqqtkzbhyyggprhovjpjyqijdrgunyxymksocskvurczbsmdelbusuqdpofskzamhklmhrrgdjqtge",
            "ynwjqmhdsstcahzioqwnlftajrnbhdembeitsczfqoztjhfaxkpojhawgtsokgzzjfyonkcsisvxqodducsnhgkclvgnyrbbfkuy",
            "qgigwnrfatzcrnrhvnczfnlcjratbkbcvnegnodqqbyuzghsbmieamvwqqlrkidicnmkjrlohjtrgkbitnpxzwsxqzbdidzaveyx",
            "bmfvderczfvirbashmriyzfrkwceebvwhpyjnlahoyzcuitkcezpnavgloycjxjaqrasckgfkwakplyyjkbzcdbhbrehwpjihngy",
            "ykcazotwzfalckzeyjxujrkvukxsjuxgilopctogqmrnvzhpsnseadhifhhjloawubvmiqvyzmynrvisnyjupjwgfzdhctrgmiov",
            "pukyolrguitgcnzddpwwpqxemttsujduonbjovqngzpbaifivisqojqztcyblerocqottjayafypdzzyvymlkrdihcvjqpawouiy",
            "ejuejeqynodrspsndrmpjkcixvjxogoprzjgyxnsctcovaubwbkqaajtfjvcmrnrkcmvspvnwesitvvnimezjcgyrjimcwnetmll",
            "xujtbtnnacezhqbzrpelbgbsnmwvuamfbvxxjjkcynsojrhlebzeptnloqgyxlfdnqcdwxfxazaxcmxkcrneiqheycgvsbgltvid",
            "qldmyynkbixpfjsdvlgfngzrhdijjxeehzebaquekjfpxofxvugnftclfcczvoqigfkievyvormswqpwvqbnobvhqjadiavgdqzw",
            "bncxmbpwuywvnaeecphfwvbpuvvknxkzsfeykeaejdrcitwtioyenzxjfsiagbsunnokmjclaffcoozgayuhjiypcmeijghndzjn",
            "rerjcjeqjvdyzzyybnbwzheozqrvjbjegzfvgwuepexsaimjtfcghoaxdsdlltahlkzneuevgnackjoohginvpqcbjxbexbqfgyc",
            "vgsskznernyntiwofhoqkntgeclhhgoyihgeeodumqnwxwrhqmgnhlubftwjwoijfymfwugxqsxwsytjctuqcxcxuhlzcllhyfri",
            "lgzsgpurzxthlzehntsvkycdavippybpnkbxjpkzdlkyxffllbydeziobquhotpbshtsoeuyoutytdyduoadxeancbnysuxzorad",
            "zjfekgidfvzzbhzoksizpcylqigaacvgqcgmzntxzrtmbucnmmrgbkbexuunvyqqnbrgnottufxpylvkbmqdocstubrfgwuqkdcn",
            "trlgbgboeszlfgadqoxwpjtkwpcrnticpxgdgyxmibjdhzrvkqzajqjhozzkiqffnwcqyuexdselwfumyyvvamiizwvztgimzgbp",
            "mlimwoskddyxunxgssfjgfcdrzbswtiyqdyamnikfhfdvfbhnltkgatdttxprfgafnufaqpzbdgmbnogesvuysqseuckbqcmpzdl",
            "nvlxantvgwrtmzzvutdjvsfftnjthfferdhejcfmhvvhunxzsijvyfigonnfrdzflvbsxnftjfxfczxoayrkouwycwvmhsfhfmyt",
            "oijzdasbaiylwkvqqmbklzbmajydkpwaglivwqqhvljvjxglkslutxjrivdgpazioaiaoobikvxlfjmizipgkhvughuoxowykuqr",
            "epyfwunrkauzbbsvuaoflozsaavyjkcuusjndiyqeatigykkbvoihfpuljqdjckemlslgdfkvmydateenrvzhavtsjrqobvvyaqo",
            "xxkfwqdzwffllyqczpnkulqzuokoogssiqyzaxehyomsgvaxzqnzflzwzzavnmibtzddwrlnuzljtojecrbbjucgyijjyinwozrj",
            "ywpjlyfbwsiognlmkszyzpxcglnlacldfjcuziemxtdeepbwewwlxfqquomlsfieomdmsiqavuqrftydpomufvewlbqvlojdmgfg",
            "xkceantgnjkiybxcvplnpxwimnprwbtwasjquwmqkrakctprjmnfdpsqjlwxuzwykuchddgsdlccgyqpolckeecgfvejderxtngo",
            "lvutlzkxcevzpqszqgdayhnyllkgrvbimougbdmgbqdzwtrddgxkwqczegfnkigphwghsosruryztixvqgrxoziiubxwoehtqoun",
            "pzorupuimoaxlyfrwweufewwucosqnrirupklqjekyktreaxgaxaqgncmwwkgwprybafuwtsagjyrawbpqeqztzdrmcpzhxcomjh",
            "eyzcwioqzvcmtxvtxxulcnxwewewbpgjyzpgcouplsctjipuwiutxhdtczetfxnnkifkvwhiamxjjppaubbwxvqrmpymzvgoevlg",
            "uasbblgcquaqcormaeupxgykzrjypwccgwbypsvxlnswbnwlixvjlzkirnlzzibkicrtlupwtoebxcemwvjkidvmlivouxiynnal",
            "nasxfhzdreqnspwuourravhdbjchfulzvgquccvevbodabeievzgvzegubfipdeoaffrgnyjdzshvtiotmjieezilwwkqhqlivts",
            "dimmqymdjhbsfkegyxfmejnczmfnmrajcxfuqymxexhmynyrxkjgpbdwmwdsckzcjymoasudsksobvebaefjngzvzqkplpoehfjh",
            "sejxqwviqhlkbartmgwsvuwruemjqpaepilbyaerwjziyecmmmeothvosfvxcyiecjxkdxfqfnmmzahndoduzhutzuhfpuszcuhv",
            "irhbaqsjmsjbwvnxhtqgocwhqqktfiquoveymoqlrussuizzmwipoudtlnrajonjmcmoqmvyqwbeznrqwrxkphozzplmnnwbygio",
            "nrvzlftzhwwfeckjtoknipjpokzwnbacdauzfnvebpapoqpyseaeyzicfsaljevtkwgivtxfjrrmocsmvimctfvrboawndjjgumy",
            "droxndceqfcpkqgmkrdeewtdxxmsgimnzsrzojkqwhavlzvpvmrtlttxhrtehcapcncxvfgxkpatabowpigzldstfbsiqwezvbww",
            "uapczwtmobvrzurhsxkodzgouxoeffgerxtxkvyaghvtzqzshqgmrrtwxkfxsisdhonyvmescqxqiltaumknxycdkzdijwkaaotg",
            "ijmsesoptcjvpducnyahcxsojqkrzjbcqwzzxfgacynhxknvkaosrnolagfiutvrwaqsxmrbofmduxrxxnxmxlaccxqzlbvrxjra",
            "veksvbkqchdgnkneqdlslicomlnnceijpsmgtaehnzsvghfabvdiwzjgdecjxsdcestuemlobekumtaxssdgzftxvjjrnhhdyfzj",
            "xtotdktrxgnvmqzxchalgdywlysribmxxjhgznotfjgtrxhilkrlsdofswlyflfzgxerykdgqdmxkyxjlopolafuznutdbzygzlx",
            "eiehlrjgmquyephjgqlmpvnxzbownzdazsyspurryzqribvlzyjigcszsuhxgtyycfwlakzaixmqorrzejooqkmrdggmkghbkesj",
            "ktataiirpttwjzyypfjsquylawvjnjtqpveynzftkxohlcwtprhvpohmrhhnhnjyjsgkgouiigliduyioqkaaavnyxpkabqehelc",
            "gacnwampmavvepmrnztqvmggpxcnbcioicwtqgalidjuqmzvobyrrnskhhccftqqxgakgwcsonkbasmpsyvixreqjyrjknwlxbdw",
            "mbvxwmfrudiujaxqnkvjwwexnphttfowstanntyfzgpztcqzzhxqhkvvqipbtqsbmjgjthyqnsbxnipvhpztlncvuevhkpbpwkxo",
            "udajfrqvjszwaqgzbblnuooxmvbtejsnhlllqajbjrgzzxooefazffzujkymnugfzxyaolprcksntajgvcbcycqzhqvvozvdoelh",
            "okqaorpeduegmjdalsmoybbdgnleozmvfvtnvzipghruarrzqqejzuzdflkjoewpzarevfrxhjoougnlccnztocotinvmebuwmtf",
            "dxrojfhlemlupcyjguhymianoxilfxgcxbfdqixvmgqeabpagmfgemhbeppewoowsljutsptrcvvtzaeyqffwbsoipwebjhssigj",
            "wssourljhoocgyrujbjgawbapexglevdtqkgdokwphlzyteycpzswblmxvxpwlkcjuiwgkppgbioyqngqjnasbofhbyrfxszhqdr",
            "hhvpfphtxnyiemyhynlwyyyjgtfsrljoglclidyxvvtrssqafossxmobcnvztpafkpuaruwzlsciirrdapmllqifqhyhaimsjrbz",
            "vjkpztaauscdovjvkyborqlaxcyjzsmgfourpyyyhtapxfxhbyyudjpdwtuwnlkfinmwghqwtvazsdkbzlzaamshyaubektppojw",
            "fjyxxtkawexosprbayitlqzyjisrdzueijomhbhlizxlnfkpapjpdyzpqemepwescbnfgghulgraenudwysqhsucjlqgujdcjjyr",
            "nsnwrrgffjtpjqufcuhndbukfpmelifvuasyyroamcjzrtvkzomxbkwlsrvmnzedhrwwgvvntxmmvzagugdzogrlxymtkdjzuhdq",
            "wcwvstsjugpaxdrlrqdctufwijfjstnwfdfgcixsvxynwrzxyojqwrmmgqqgrwumcfxgzifgdlrqdwoltdtfoyyalzlnyziblpek",
            "qgjnrxxigdlryhbknxmaqexsjabtrofromjudzyubsyxjcifjjyqchgomlgcpxwvxxdrrpcfbuuijxdwukwumdvunbnlkmobxcsc",
            "mueqpapmemzbrklixyhmubxhdxhzzhbakytecctcqahmruljqsleaedvqyybrkxmshliywgxlfuhxpbjmcwpoqrhbkrdlxuphncf",
            "djbzfihlhqeswuegjyxxthddepzqflfnhkyckjenevfcbxagwvxqplmajqctayqlbdnlgbptmaosepfbdcxkptkaxnntnxzqozxv",
            "jtvuxxetpjvdncairjsvzphhblrxvpvficztkgphkspptvzdhrqphhydgcnysuwzkxalsucwmfsqxbkgkxaxkajesiyywgecsxai",
            "cdpbumrfxufyzpxdhfkuogbgtuwoqwmxffomzkvfuicdahjvirwqkrnseiltuetvtbxkwmprbziietgrvbzwmgxxmsjrbvmyulks",
            "cyyktczgcgjxekttrkmigjqrawlnlpudzavedpsketuoerledqftnkrkralkpxtzvgetimtztwpqrwvwfsriwlemljgqqagokrus",
            "vlkzbmcrdvbrutlbtvntvdplgsdnxhjskvnptsjdepnuiivpefjnjhprqjssgsoemeiwuqrggchgkjabcqxrqaqohkruhbjnfcvt",
            "uaqbfmjjrnqfvvfsuybubxkkjgxacwnjbrwmnpcbbnlriyaqcfeekdosmaohfmplrltoxflmhnsmuatdvxwyzrwlszlvwxzgvvxg",
            "hkvdhjzwhykxsnqdlrhgfojcpwlughuqbpsznsgffzuergznmpdksgycrqmnruihbbavuosjvnwxxpmnautiudmgalztxoczqoka",
            "kpkbaedgiyzaroyxsfakegglmwgfxoreoaycxvjtjnzkdidjglzhlnzsgfoemkcdpkcuigafemvuvfjcdtqpfpkyjuneilabthcx",
            "ebycypouydpptxjsggahkbvnchwlegdfdclkremybnomyfjnnzjvwrgpxdymtwxhuvgajquqgfqcpdbrmfwwjpvxgrxcabewwqjn",
            "xnhqueqqpvsayorjsgudtghmdfgycbuakukmdequrezaqtuojmicaxcpfkfxsoctgrbziicpenckxitdsxevmgzctgsdhkbxjsfb",
            "podtoqisfeuuydukdjrhzjiafupdibkcbgrkzfafilrlwwvchfwksqyrwizakxxmquwjboqqkprdxwblzzgsrqviyeaxvckuqmxx",
            "jegfkvmxouyukzdpwnxdaovvfavxdmgfaotqbijxdwkyxzqjpggtwhiguefekcgqrzlyofodjoittschlurcdamlgjwwsvlhicfx",
            "omhmmohcfdmzkaahbmwwnmuclhvfnjsfozxcndelgyibfljbxldpjuprpsmjzfrcrdmeaqlnahcphjvionmidxuzwjziggsrymuq",
            "urtoodmqotufmyrgkvvlplcpqrmgjqtwnsxubzxzcdyrfurhlzhvycgoivncoteplodztiugoncputkbelracwgwqsmzumtnqazx",
            "zmjlpylrliiwbihsjsanaazofhsjagkunaanexpnrkxvwnmfneaficratlgvgmojwzonpczjbybynmiqsklagfyksrxveetmokxt",
            "saeqogjrdooixctqlgalayioezshxoxmzwuzgsbnkktlogfvvsajuwoepqvlpjwqcbgnsmmlbusgirlzzbngiiagzvwgxlureiyh",
            "bteycsnlukwjaxqgwxlqrcyxueykznnxjzpkpeafuoorjrymrqevfaqfczpabmolgamoegiprphpnuyswvmreruyacmqipwulphn",
            "jaboldifpcohlpigojohzlrokaqkjpawhylpzktmwsqqylfddjcobbhiudsuermrbfklqowvqshwgrhqqutovxdqujaxrapmgcvn",
            "guugpqwaktbjuowrwqprgmhlgmiqxifbjvjyfvhtmpydasmgitzzzcgnctyckzsohlwmfyopsdemdblrkhkjhubmqpcnqatijgdv",
            "ugvhvmurdhblohmvjxbdxemzqrwxekbbogjsfebjucoxxqmlzusvihpxuettmhjraroyklrxsjtwacwrfgxfvetcxribrshtbrzr",
            "luxgfrjcsqmurdlzkactiqvmximtiskkwzydehsthhyplbnhrcccczayczwolxszolqgouaftebwpapxukeqcyjokvvzlwpfnjlu",
            "izskskqbrrmvomzrcjezunmzchljddiqqznhqlgeycpzpdzkgwlqplewpqyfskitalevfsuyytdkvgfqzqgoxsbsleitmwpofwax",
            "wvkmmniagtilhzxyjdiygqbzanjqrhfxmmkzhdtkfebexdusgjszwamcvxyveansmqpnfmydczzpmxtlxkbpljcjxrtrrftiepsg",
            "oruykgciordgafzgnecforlmsffpvqwhciawolaxwqyxuhgrkzkkyacxxrcwtquaewnwssroctfbkuigrlutetjjejkbgnphtiwt",
            "uwympkgqzyevazokvbykabpmgfandumwsmqfiovjwougsglifctzeifnvgiikuereayvvilzrcwphkhhfxcxhnmuukwqrilpicxg",
            "iibipamzyznjhicfdibpdnbxynsazmtgszimvmnlkzeidzzjynoojcuuyfljdwsnjupoujuhwbprllxciruyijvxxhpzscgormur",
            "wcvtavkujkgsjvxqnmvoiocyxqcmvargirtngaeubransrjzynzqywtudugdwyeupnraptwjjffyonrqeuxeqgyreqhelkhvxebt",
            "cnqzxqrnztogafefllnooldvzdsuvqfgwwpouvgqcmmlxbksqgjddsouzupaxhafjogryatvnsrmgtlwgchdogdoupsbsbglhdzd",
            "ufnneunxpecjduyiwdzjrwirtgffhrwjiehhjblrcevtpvjxzpkrkprbxgcnvvqbayyrjvudrtgdhpugljpdbziqczwtrnuxlaht",
            "ljtbzjgnemfjdkrtzmtbypymrpwckgksaxvhivsylevfoznwnwbrjfknrrxgqfxvewhqxoiexlzgdcpanxfzupztzemkbezpjbpo",
            "cxirqwcyzjdjqqgotntbxyobemvskwwpfchskzuewaolcambienmubdanhkuxcgenkypzrdlxfsohmwnoynbehgcxztrnxrmfhst",
            "tihyhgzhskgzfhxatpronphslvsyhpcttwqqgdydcbzsmeoujlbhcnclaohphekvwuhqfquxpcktxqlxpfhfehksocgvfvxcwery",
            "btpuhxgofircivkkjqzdjxreazftdtnyylobbbxgswskewxyycnsivjdrwijzkzhpyucdfikwqshookugwrcedzafxheuhpichut",
            "tvqttikfjrbskmwjqtbyavmovyzeeagtjxxhklquyfruwurbsifvvywusfqiblokjpqbeqmawilxgmvhmmimyfrqfhomcbjsxvgd",
            "rgzrgbihpdckrqarsylkklmnevpgqhitnzyaigntuijzkxtncqhksmunyjrzmlwmldlhfthajvklatvlcgfoewzlrufmuipnzihm",
            "rewrgpzcfycoclwwzctcubmibztupbgbdsqpvgidgpyzsrplrzsftreapamshhchojthagpgyefgmnlmcactiapvnhnqhytmznvr",
            "smlywmmixzagjnyjyftddnajcwtxzsgzciqyzoojkutsagnmmwxfdbhqhyzvdufhfbpeqjvdakshjblgjdahpotznhuessuiklae",
            "vqwxiktrzpllggpfhyzxpvsadeteueapiixzmorruxheofxuzexbktrzyuehqwflufvwqisffnotrirxbcpaconyfdaykglfxavp",
            "airidyzwwudqytasdzwiexpiyzgnhgclzlyojxrzptucbkfksarxkcvqlhxurlzkjbarurxolakwihgspsiggyyvgiuhphkzezaw",
        ]), ["g", "z"]),
    ])
