x<-seq(-5,5,0.1)
x2<-seq(-4,qt(0.125,10),0.1)
x3<-seq(qt(0.875,10),4,0.1)

plot(x,dt(x,10),type="l",xlim=c(-5,5),ylab="dt",col="red",main="t分布のグラフ")

par(new=T)
plot(x2,dt(x2,10),axes=F,type="h",col="red",xlim=c(-5,5),ylim=c(0,0.4),lwd=2,xlab="",ylab="")
par(new=T)
plot(x3,dt(x3,10),axes=F,type="h",col="red",xlim=c(-5,5),ylim=c(0,0.4),lwd=2,xlab="",ylab="")

abline(v=qt(0.125,10),col="red",lty=2,xlim=c(-4,4))
abline(v=qt(0.875,10),col="red",lty=2,xlim=c(-4,4))

par(new=T)
plot(x,pnorm(x,0,1),axes=F,type="l",col="green",ylim=c(0,1),lwd=2,xlab="",ylab="")
axis(4)

mtext("分布関数",side=4,line=3)
labels<-c("dt","pt")
cols<-c("red","green")
lts<-c(1,1)
legend("topleft",legend=labels,col=cols,lty=lts)