import os,json,urllib.request as q
V=[0,100,320,330,500,900,0];N=[-21,-19,-12,-8,8,12,19,21];J=[-11,-10,-9,-1,1,9,10,11];Y=[-11,-9,9,11];Z=[-10,-1,1,10]
T='KKKKUUUUMMOQLLMPKKKOLJIKLMMGKKKKACEECGKKEKMNELNOEKNOELMNCGKLACEEGIIIIKKKIKLMILLMIKMMIMMMILKKGIIIKKKKLMMMJKKKJKKKJKKKJKKKJKKKKKKLGIIJIKKKIKLLJKLLKKLLILLLIKLKGIIJECCAECCAECCAECCAGEECIGGGOOKKOQMK'
def H(d,t):
 a=abs(d);u=t//10-2;r=u if d>0 else 7-u;f=t%10-1;q=min(f,7-f)
 return(V[a]+(ord(T[(a-1)*32+r*4+q])-75)*5)*(d>0 or-1)
M=9999;L=[0,0,N,Y,Z,J,J];TT={};C={91:2,98:1,21:8,28:4,95:3,25:12}
def F(f):
 w=f.split();B=[9-9*(21<=i<99 and i%10 not in(0,9))for i in range(120)]
 i=21;s=0
 for c in w[0]:
  if c=='/':i+=2
  elif c.isdigit():i+=int(c)
  else:
   d='PNBRQK'.find(c.upper())+1
   if c.islower():d=-d
   B[i]=d;s+=H(d,i)
   i+=1
 a=B.index(6);b=B.index(-6)
 d=1 if w[1]=='w' else-1;c=sum({'K':1,'Q':2,'k':4,'q':8}.get(x,0)for x in w[2])
 e=w[3]!='-'and ord(w[3][0])+4-10*int(w[3][1])
 return[B,d,c,e,s,a,b]
def A(B,t,s):
 if s in(B[t+11*s],B[t+9*s]):return 1
 for d in N:
  if B[t+d]==2*s:return 1
 for d in J:
  if B[t+d]==6*s:return 1
  j=t+d
  while B[j]==0:j+=d
  x=B[j]
  if x in(5*s,(3+(d not in Y))*s):return 1
 return 0
def G(p,Y=0):
 B,s,c,e=p[:4];m=[];pr=2+7*(s<0);sr=8-5*(s<0)
 for i in range(21,99):
  v=B[i]
  if v*s<=0 or v==9:continue
  a=abs(v)
  if a==1:
   j=i-10*s
   if B[j]==0:
    m.append((i,j,5*s*(j//10==pr)))
    k=i-20*s
    if not Y and i//10==sr and B[k]==0:m.append((i,k,0))
   for d in(-11*s,-9*s):
    j=i+d
    if -9<B[j]*s<0 or j==e:m.append((i,j,5*s*(j//10==pr)))
  else:
   Y2=L[a];l=2<a<6
   for d in Y2:
    j=i+d
    while B[j]==0:
     if not Y:m.append((i,j,0))
     if not l:break
     j+=d
    if -9<B[j]*s<0:m.append((i,j,0))
   if a==6 and not Y:
    k=25+70*(s>0)
    for d in(1,-1):
     t=k+2*d;rf=k+3-7*(d<0);b=1<<(d<0)+(s<0)*2
     if i==k and c&b and B[k+d]==B[t]==0 and(d<0)*B[k-3]==0 and B[rf]==4*s and not any(A(B,x,-s)for x in(k,k+d,t)):m.append((k,t,0))
 return[x for x in m if not A((n:=K(p,x))[0],n[5+(s<0)],-s)]
def K(p,m):
 B,s,c,e,v,w,b=p;f,t,pr=m;N=B[:];q=B[f];d=B[t];y=t
 if abs(q)<2 and t==e:y=t+10*s;d=B[y]
 N[f]=0;v-=H(q,f)
 if d:N[y]=0;v-=H(d,y)
 if abs(q)==6 and abs(t-f)==2:
  z=(t>f)*2-1;rf=f+3-7*(z<0);rk=q//6*4;N[rf]=0;v-=H(rk,rf);N[f+z]=rk;v+=H(rk,f+z)
 n=pr or q;N[t]=n;v+=H(n,t);a=c&~(C.get(f,0)|C.get(t,0))
 if q==6:w=t
 if q==-6:b=t
 return[N,-s,a,(f+t)//2*(abs(q)==1 and abs(t-f)==20),v,w,b]
def O(p,ms,tt=None):
 B=p[0]
 def sc(m):
  f,t,pr=m;cap=B[t]
  if abs(B[f])<2 and t==p[3] and cap==0:cap=1
  if m==tt:return-19999
  if cap:return-1000-V[abs(cap)]*10+V[abs(B[f])]//10
  if pr:return-900-V[abs(pr)]
  return 0
 return sorted(ms,key=sc)
def S(p,d,a,b):
 global NN;NN+=1
 if NN>=NL:return p[4]*p[1]
 k=(tuple(p[0]),p[1]);v=TT.get(k)
 if v and v[0]>=d and(v[3]<1 or v[3]==1 and v[1]>=b or v[3]>1 and v[1]<=a):return v[1]
 if d<=0:
  s=p[4]*p[1]
  if s>=b:return b
  if s>a:a=s
  for m in O(p,G(p,1)):
   z=-S(K(p,m),-1,-b,-a)
   if z>=b:return b
   if z>a:a=z
  return a
 ks=p[5+(p[1]<0)];h=A(p[0],ks,-p[1])
 if not h and d>=3 and b<9000:
  n=p[:];n[1]*=-1;n[3]=0
  if -S(n,d-3,-b,-b+1)>=b:return b
 ms=G(p)
 if not ms:return-M if h else 0
 ms=O(p,ms,tt=v and v[2]);be=-M-1;bm=ms[0];a0=a
 for m in ms:
  z=-S(K(p,m),d-1,-b,-a)
  if NN>=NL:return be if be>-M-1 else p[4]*p[1]
  if z>be:
   be=z;bm=m
   if z>a:
    a=z
    if a>=b:break
 TT[k]=(d,be,bm,1 if a>=b else 2*(be<=a0));return be
def R(p,n):
 global NN,NL;NL=n;TT.clear()
 rm=G(p);bm=rm[0];NN=0;d=1
 while NN<NL:
  be=-M-1;cb=bm
  for m in O(p,rm,tt=bm):
   z=-S(K(p,m),d-1,-M-1,-be)
   if NN>=NL:break
   if z>be:be=z;cb=m
  else:bm=cb;d+=1;continue
  break
 return bm
def main():
 U=os.getenv("MAKEFUN_ENV_URL");NB=int(os.getenv("NODE_BUDGET",50000))
 def P(a,b):return json.load(q.urlopen(q.Request(U+a,json.dumps(b).encode())))
 while(g:=P("/game",{}))["status"]!="done":
  while g["status"]=="your_move":
   p=F(g["fen"]);m=R(p,NB);f,t,pr=m;s=''.join(chr(96+x%10)+str(10-x//10)for x in(f,t))
   if pr:s+='q'
   g=P("/move",{"game":g["game"],"move":s})
if __name__=="__main__":main()
