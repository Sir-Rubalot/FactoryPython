Detta program simulerar en anbetsplats där anställda skriver in sitt namn för att stämpla in och sedan klockslaget de börjar jobba.
Samma sak för att stämpla ut, man skriver in sitt namn och klockslaget man slutar jobba (detta tar bort anställd från databasen också).


För att köra programmet då:
1. Starta upp VS code eller annan editor. 
2. Öppna upp mappen Factory. 
3. Markera filen "app".
4. I terminalen ska du skriva "python -m app.main" för att den ska köra rätt fil. 
5. Nu bör du kunna köra main-programmet i terminalen. 



Jag hade lite problem med filstrukturen, eller snarare importeringen mellan klasserna och att dela upp logiken i olika klasser och sedan påkalla dem i ytterligare en klass (main), det resulterade i att jag började om helt och hållet med en ny mappstruktur och jag började med att göra hela worktree'et innan jag gjorde en virtual environment i app-filen så alla filer räknas in. 
Jag har lärt mig mycket med logiken i python genom detta program och inte minst när jag brottades med json och att skriva till och hämta från databasen, men nu i efterhand har det varit riktigt belönande att ha det klart och allt fungerar. 
Efter nästa kurs, databasteknik hade jag velat gå tillbaka till detta program med mer kunskap och snygga till vissa funktioner som kanske är lite kladdiga i nuläget. 