class counter(object):
    """intensityFile can be a LIST or a FILE(ADDRESS to file). please surround the address with ''. 
    format can be '.p' or '.txt' """
    
    def __init__(self,intensityFile,format=''):
        
        
        if type(intensityFile) is list:
            self.intensity=intensityFile
        
        elif type (intensityFile) is str:
            
            
            self.fileFormat='unknown'
            
            
            if format!='':
                if format =='.p' or format =='pickle':
                    self.fileFormat='.p'
                elif format =='.txt' or format=='text':
                    self.fileFormat='.txt'
                else :
                    print 'Sorry. File format specified not supported or invalid.\n Please use .txt or .p as format.\n Going into auto mode.'
            
            
            elif format=='' or self.fileFormat=='unknown':      #auto mode
                if intensityFile.split('.')[-1]=='p':
                    self.fileFormat='.p'
                elif intensityFile.split('.')[-1]=='txt':
                    self.fileFormat='.txt'
                else :
                    print"defaulting to .txt"
                    self.fileFormat='.txt'
                
            self.intensity=self.parse(intensityFile,self.fileFormat)



    def parse(self,filename,format):
        f=open(filename,'r')
        if format =='.p':
            print 'not implemented'
            raise()
        elif format =='.txt':
             print 'not implemented'
             raise()

    def countred(self,retpeaklst=False):
        count=0
        self.peaklistr=[]
        self.intensityr=[point[2] for point in self.intensity]
        self.cutoff=sum(self.intensityr)*1.0/len(self.intensityr)
        for i in range(len(self.intensityr)-1):
            if self.intensityr[i]<self.cutoff and self.intensityr[i+1]>self.cutoff:
                count+=1
                self.peaklistr.append(250)
            else:
                self.peaklistr.append(0)
                
        if retpeaklst:
            return count,self.peaklistr
        return count
    def countgreen(self,retpeaklst=False):
        count=0
        self.peaklistg=[]
        self.intensityg=[point[1] for point in self.intensity]
        self.cutoff=sum(self.intensityg)*1.0/len(self.intensityg)
        for i in range(len(self.intensityg)-1):
            if self.intensityg[i]<self.cutoff and self.intensityg[i+1]>self.cutoff:
                count+=1
                self.peaklistg.append(250)
            else:
                self.peaklistg.append(0)
                
        if retpeaklst:
            return count,self.peaklistg
        return count
    def countblue(self,retpeaklst=False):
        count=0
        self.peaklistb=[]
        self.intensityb=[point[0] for point in self.intensity]
        self.cutoff=sum(self.intensityb)*1.0/len(self.intensityb)
        for i in range(len(self.intensityb)-1):
            if self.intensityb[i]<self.cutoff and self.intensityb[i+1]>self.cutoff:
                count+=1
                self.peaklistb.append(250)
            else:
                self.peaklistb.append(0)
                
        if retpeaklst:
            return count,self.peaklistb
        return count