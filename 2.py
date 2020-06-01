import math

class Point3d(object):
     def __init__(self, X=0,Y=0,Z=0):
         self.xCoord=X
         self.yCoord=Y
         self.zCoord=Z
     def  getX(self):
         return self.xCoord
     def  getY(self):
         return self.yCoord
     def  getZ(self):
         return self.zCoord
     def  getXYZ(self):
         return self.xCoord, self.yCoord, self.zCoord
     def setX(self, A):
         self.xCoord=A
     def setY(self, B):
         self.yCoord=B
     def setZ(self, G):
         self.zCoord=G
     def equals(self, O):
         return O[0]==self.xCoord ,O[1]==self.yCoord ,O[2]==self.zCoord 
     def distanceTO(self,O2):         
         return  math.sqrt(((O2[0]-self.xCoord)**2) +((O2[1]-self.yCoord)**2)+((O2[2]-self.zCoord)**2))
     def distanceTO(self,O2):         
         return  math.sqrt(((O2[0]-self.xCoord)**2) +((O2[1]-self.yCoord)**2)+((O2[2]-self.zCoord)**2))
     def treangle(self, Tr1):
         p=0.5
         x1=Tr1[0]-Tr1[2]
         x2=Tr1[1]-Tr1[2]
         y1=self.xCoord-self.zCoord
         y2=self.yCoord-self.zCoord
         if( 0 > p*(x1*y2-x2*y1)):
             return -p*(x1*y2-x2*y1) 
         else:
             return  p*(x1*y2-x2*y1)
                 
     
a= Point3d(7,4,3)
b= Point3d(17,6,2)
print(a.treangle(b.getXYZ()))        
        