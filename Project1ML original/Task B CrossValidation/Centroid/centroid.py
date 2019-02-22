

# @author:Arpit Saxena
"""
"""numpy used only to load data and write data to the file"""
import numpy as np
def Euclidean(A_train,B_test):
    train_i=0
    test_i=0
    distance=0
    while(train_i<len(A_train) and test_i<len(B_test)):
        distance=distance+(((A_train[train_i]-B_test[test_i]))**2)
        train_i+=1
        test_i+=1
    distance=distance**0.5    
    distance=('%.2f' % distance)
    return float(distance)

#Centroid
centroidList={}
def Centroid(trainXdata,trainYdata):
    centroidListArray=[]
    for o in range (0,len(trainXdata[0])):
        sum=0
        for p in range(len(trainXdata)):
            sum+=(trainXdata[p][o])
        centroidListArray.append(float('%.2f'%(sum/len(trainXdata))))
    a=trainYdata[0]
    centroidList[a]=centroidListArray 
class dataHandler(object):
    def pickDataClass(self,filename,class_ids):
        filename1=np.loadtxt(filename,delimiter=',')
        finaldata=[]
        self.lenclassids=len(class_ids)
        for i in range (len(filename1[0])):
            if filename1[0][i] in class_ids:
                finaldata.append(filename1[:,i])
            else:
                continue
            q=np.stack(finaldata)        
        return q
    
    def splitData2TestTrain(self,filename, number_per_class, test_instance):
        test_instance=test_instance.split(':')
        self.lead=int(test_instance[0])
        self.trail=int(test_instance[1])
        self.lead1=int(test_instance[0])
        self.trail1=int(test_instance[1])
        testdata=[]
        traindata=[]
        
        max=number_per_class
        min=0
        while max<=len(filename[0]):
            testdata.append(filename[:,self.lead:self.trail])
            traindata.append(filename[:,min:self.lead])
            traindata.append(filename[:,self.trail:max])
            self.lead+=number_per_class
            self.trail+=number_per_class
            max+=number_per_class
            min+=number_per_class
            
            
        testdata=np.hstack(testdata)
        traindata=np.hstack(traindata)
        return(testdata,traindata)
    #use only in there are letters    
    def letter_2_digit_convert(self,string):
        self.array = []
        for x in string:
            self.array.append(ord(x)-64)
        self.array=np.stack(self.array)
        return(self.array)

    def main(self,a,b):
        s=''
        s=s+str(a)
        s+=':'
        s+=str(b)
        datahandler=dataHandler()
        dataset=datahandler.pickDataClass('ATNTFaceImages400.txt',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40])
        dataset=dataset.transpose()
        number_per_class=10
        
        testdata,traindata=datahandler.splitData2TestTrain(dataset,number_per_class,s)
                                                            
        
        trainX=traindata[1:,:].transpose()
        trainY=traindata[0,:,None]
        testX=testdata[1:,:].transpose()
        testY=testdata[0,:]
        
        
        ele=0
        count=0
        #divide by number of labels
        
        for cen in range(datahandler.lenclassids-1):
            while trainY[ele]==trainY[ele+1]:
                ele+=1
            Centroid(trainX[count:ele+1,0:],trainY[ele]) #number each label
            ele+=1
            count=ele
        Centroid(trainX[ele:,0:],trainY[-1])
        
        
        cdistances=[]#distances of each testing instances from the centroids
        for k in range(len(testX)):
            cdistances.append({})
            for elements in centroidList:
                cdistances[k][elements]=Euclidean(centroidList[elements],testX[k])
        
        finalclassifier=[]
        for elements in cdistances:
            leastdistance=min(elements.values())
            for key,val in elements.items():
                if val==leastdistance:
                    finalclassifier.append(key)
                    break
        
        #error test and accuracy
        error = testY - finalclassifier
        TestingAccuracy = (1-np.nonzero(error)[0].size/len(error))*100   
        return(finalclassifier,TestingAccuracy)


        
    #change indexes
    
a=dataHandler()
classification1,accuracy1=a.main(0,2)
np.savetxt('Classification output 1',classification1,fmt="%0.0f")
f1=open('Classification output Accuracy 1','w')
f1.write('%f'%accuracy1)
f1.close()
classification2,accuracy2=a.main(2,4)
np.savetxt('Classification output 2',classification2,fmt="%0.0f")
f2=open('Classification output Accuracy 2','w')
f2.write('%f'%accuracy2)
f2.close()
classification3,accuracy3=a.main(4,6)
np.savetxt('Classification output 3',classification3,fmt="%0.0f")
f3=open('Classification output Accuracy 3','w')
f3.write('%f'%accuracy3)
f3.close()
classification4,accuracy4=a.main(6,8)
np.savetxt('Classification output 4',classification4,fmt="%0.0f")
f4=open('Classification output Accuracy 4','w')
f4.write('%f'%accuracy4)
f4.close()
classification5,accuracy5=a.main(8,10)
np.savetxt('Classification output 5',classification5,fmt="%0.0f")
f5=open('Classification output Accuracy 5','w')
f5.write('%f'%accuracy5)
f5.close()
AverageAccuracy=(accuracy1+accuracy2+accuracy3+accuracy4+accuracy5)/5
f6=open('AverageAccuracy','w')
f6.write('%f'%AverageAccuracy)
f6.close()


           
           
           
           
           
