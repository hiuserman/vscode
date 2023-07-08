x<-seq(-0,20,0.1)
df<-3
plot(x,dchisq(x,df),xlim=c(0,20),type="l",ylab="dchisq(x)",col=1,lty=1,main="カイ2乗分布のグラフ")
abline(v=qchisq(1-0.05,df),lty=2,col="red",xlim=c(0,20))
par(new=T)
x2<-seq(qchisq(1-0.05,df),20,0.2)
plot(x2,dchisq(x2,df),axes=F,type="h",col="red",xlim=c(0,20),ylim=c(0,0.25),lwd=2,xlab="",ylab="")

