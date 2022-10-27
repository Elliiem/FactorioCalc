


ItemList = dict()
f = open("ItemData.txt")

#Convert ItemData File to Dict
for lines in f:
 ItemData = lines.split("-")
 ItemName = ItemData[0]
 ItemData.pop(0)
 ItemData.pop(-1)
 ItemList[ItemName] = ItemData


#-----------------------------------------------
#Innit Stage Mod
def Querry(Item,qnt):
 #Innit
 Stage = 1
 StageList = [Item,float(qnt)]
 StageList.insert(2,("STAGE"+str(Stage)))
 Stage += 1
 IngList = [Item,float(qnt)]
 i = 0
 #Construct StageList
 while i == 0:
     #Get Ing and Update
     NextStage = GetNextStage(IngList)
     IngList = NextStage
     #Check if NextStage is Empty
     if IngList == []:
         i=1
         break
     #Add Stage to List
     StageList = AddStageList(StageList,IngList,Stage)
     Stage += 1
 #"Start Calc"
 print (StageList)
 GetStages(StageList)

#Fetch Ingrediends
def GetIng (Item,qnt):
 #Innit
 IngReturn = []
 ItemData = ItemList[Item]
 IngStr = ItemData[-1]
 IngList = IngStr.split("*")
 #Get Num/Name
 for x in range(0,len(IngList),2):
     if float(IngList[-1]) != 0:
         Name = IngList[x]
         Num = float(IngList[x+1])*qnt
         IngReturn += Name,Num
 #Return
 return IngReturn

#Fetch Next Stage Ing     
def GetNextStage(IngList):
 #Innit
 NextStage = []
 #Get Ing from List and Add to New List
 for x in range(0,len(IngList),2):
     NextStage += GetIng(IngList[x],IngList[x+1])
 #Return
 return NextStage

#Add Stage to List
def AddStageList(List,NList,Stage):
 #Add Items from NList to List
 List += NList 
 #Add Stage Num
 List.append ("STAGE"+str(Stage))
 #Return  
 return List

#----------------------------------------------
#Get Machines
def Machines(Item,qnt):
    #Innit
    ItemData = ItemList[Item]
    Time = float(ItemData[0])
    Ammount = float(ItemData[1])
    Station = ItemData[2]
    
    Count = (Time*qnt)/Ammount    
    return [Count,Station]

#Get Stages
def GetStages(StageList):
    Stage = []
    for x in range(0,len(StageList)):
        if(str(StageList[x]).__contains__("STAGE")):
            HandleStage(Stage)
            Stage = []
        else:
            Stage.append(StageList[x]) 

#Out Stage Data
def HandleStage(Stage):
 for x in range(0,len(Stage),2):
        Machine = Machines(Stage[x],Stage[x+1])
        print("-------------------")
        print (Stage[x])
        print(str(Machine[0])+" - "+Machine[1])
        print("-------------------")

#-----------------------------------------------



Querry("Iron_Test",5)
