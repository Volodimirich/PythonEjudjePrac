#Интерпретатор НАМ с дополнительными фунциями (повторная работа, чтение из нового файла, работа в режиме)

import collections
import sys

class Exc(Exception): pass

RuleMes="You want to change some rule, are you sure?\n"+"yes - 1, no - 0\n"
ModeMes="Choose an operating mode\n"+"Normal - 0, Interactive with the ability to add rules - 1\n"
RepMes="How about one more time?\n"+"yes - 1, no - 0\n"
RFileMes="Do you want work with the same file?\n"+"yes - 1, no - 0\n"

def AddRule(RDict,Str,Forse):
    PosN=Str.find("->")
    PosT=Str.find("=>")
    
    if PosN==-1 or PosT==-1:
        Pos=max(PosN,PosT)
        Flag=1 if PosT>PosN else 0 
    else:
        ErrMes="Error: You have -> and => in one rule"
        raise Exc(ErrMes)
    
    if Pos<0:
        ErrMes="Error: Non a rule here - "+Str
        raise Exc(ErrMes)
    
    if not RDict.get(Str[:Pos]) or Forse:
        arg = Str[:Pos] if Pos>=0 else ""
        Off=-1 if Str[-1]=='\n' else None
        RDict[arg]=(Str[Pos+2:Off],Flag)

    return RDict


def GetRules(FName):
    RuleSav=collections.OrderedDict()
    File=open(FName,'r')
    
    for line in File:
        RuleSav=AddRule(RuleSav,line,False)
        
    return RuleSav


def CheckArg(Arg):
    if Arg=="0":
        return False
    
    if Arg=="1":
        return True
    
    ErrMes="You selected an invalid option"
    raise Exc(ErrMes)


def InteractiveMode(RDict,Total,Time):
    Mode=False
    print(Total)
    Mes="" if Hops else "You can add some rules here - "
    Str=input(Mes)
    
    if Str:
        Pos=max(Str.find("->"),Str.find("=>"))
        
        if RDict.get(Total[:Pos]):
            Mode=CheckArg(input(RuleMes))
            
        RDict=AddRule(RDict,Str,Mode) 
    return RDict


FlagRep=True
FlagFile=False
Name=""
MaxHops=1024
while FlagRep:
    Name=Name if FlagFile else input("Input file name with rules - ")
    InStr=input("Ok, and just now input some string - ")
    WordSet={InStr}
    
    try:
        WorkMode=CheckArg(input(ModeMes))
        Rules=GetRules(Name)
    except Exc as Mes:
        print(Mes)
        sys.exit()
        
    Hops,Step=0,0
    OkFlag=True
    
    while OkFlag:
        
        if not Step:
            if WorkMode:
                print(Hops)
                Rules=InteractiveMode(Rules,InStr,Hops)
            else:
                print(InStr)
                
        if Hops>MaxHops:
            OkFlag=False
            print("Error: Step limit reached")
            
        if Step<len(Rules):
            LRule,(RRule,stop)=list(Rules.items())[Step]
            Pos=InStr.find(LRule)
            
            if Pos<0:
                Step+=1
            else:
                InStr=InStr.replace(LRule,RRule,1)
                Hops+=1
                
                if stop:
                    break
                else:
                    Step=0
                
                if InStr in WordSet:
                    OkFlag=False
                    print("The sequence loops, bad word is - ",InStr)
            WordSet.add(InStr)
        else:
            break
        
    if OkFlag:
        print("Result is - ",InStr)
        
    try: 
        FlagRep=CheckArg(input(RepMes))
        
        if FlagRep:
            FlagFile= CheckArg(input(RFileMes))
            WordSet.clear()
            Rules.clear()
            
    except Exc as Mes:
        print(Mes)
        sys.exit()
        
print("Have a nice day!")
