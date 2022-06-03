library(ggplot2)
library(gtools)
library(grid)
library(gridExtra)
library(cowplot)

setwd('C:/Users/cecko/Desktop/Computational Project/Diplostomida/Simulation/')

likes_files <- list.files(pattern='mcmc_likes_*')
likes_files <- mixedsort(likes_files)
likes <- data.frame()
for(i in 1:length(likes_files)){
  likes_current <- read.table(likes_files[i])
  likes_current$V1 <- ((i-1)*1500+1):(i*1500)
  if(i==1){
    likes <- likes_current[1501:3000, ]
  }
  else{
    likes <- rbind(likes[ ,1:2], likes_current[1501:3000, ])
  }
}
likes$run <- rep(0:19, each=1500)

pdf('diplostomida_sim.pdf')
ggplot(likes) + geom_point(aes(x=V1, y=V2, colour=as.factor(run))) +
  theme(axis.title.x = element_blank(), axis.title.y = element_blank(),
        panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = 'black'),
        axis.text.x = element_blank(), axis.text.y = element_text(size = 28),
        plot.title = element_text(hjust = 0, size = 28),
        legend.position = 'none', legend.title = element_text(size = 28),
        legend.text = element_text(size = 28)) +
  ggtitle('d)') +
  labs(colour = 'Run number')
dev.off()

pdf('legend.pdf')
legend <- get_legend(plot)                    
grid.newpage()                              
grid.draw(legend) 
dev.off()
