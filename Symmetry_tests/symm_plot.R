library(tidyverse)
setwd('C:/Users/cecko/Desktop/Computational Project')

#change file name
files <- list.files (pattern = 'NKResults_rate_.+_internal.txt')
symm_results <- data.frame()
for (i in 1:length(files)){
  current_results <- read.table(files[i])
  if(i==1){
    symm_results <- current_results
  }
  else{
    symm_results <- rbind(symm_results, current_results)
  }
}

symm_results$InternalBrLen <- rep(c(0.01, 0.1, 0.2, 0.5, 1.0), each = 100)
colnames(symm_results)[1:6] <- c('A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D')
symm_results <- pivot_longer(symm_results, names_to = 'Comparison',
                             values_to = 'p_value',
                             cols = c('A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D'))

summ_results <- symm_results[symm_results$Comparison!='A-C'&
                                symm_results$Comparison!='B-C', ] %>%
  group_by(InternalBrLen, Comparison) %>%
  summarise(mean = mean(p_value), sd = sd(p_value))

for(i in 1:length(unique(symm_results$Comparison))){
  mod <- lm(data = symm_results[symm_results$Comparison ==
                                  unique(symm_results$Comparison)[i], ],
            p_value~InternalBrLen)
  print(unique(symm_results$Comparison)[i])
  print(summary(mod))
  print(anova(mod))
}

#change file name and title
pdf('symmPValues_rate_internal.pdf')
ggplot(summ_results, aes(x = InternalBrLen, y = mean, group = Comparison)) +
  geom_line() + geom_point(aes(shape = Comparison, size = 3)) +
  theme(axis.title.x = element_blank(), axis.title.y = element_blank(),
        legend.position = 'none', panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(), panel.background = element_blank(),
        axis.line = element_line(colour = 'black'), axis.text.x =
          element_text(size = 28), axis.text.y = element_text(size = 28),
        plot.title = element_text(hjust = 0, size = 28)) + ylim(0, 0.6) +
  ggtitle('e)')
dev.off()
