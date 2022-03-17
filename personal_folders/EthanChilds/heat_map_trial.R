library(readr)
library(tidyverse)
library(ggplot2)

core_poi_patterns <- read_csv("raw_data/ID-CORE_POI-PATTERNS-2021_07-2021-10-18/core_poi-patterns.csv")
View(core_poi_patterns)

core_poi_patterns

keeps <- c('latitude', 'longitude', 'raw_visit_counts', 'raw_visitor_counts')
heat_map_df <- core_poi_patterns[keeps]
heat_map_df

ggplot() +
  geom_point(data = heat_map_df, aes(x = longitude, y = latitude), alpha = .05)

             
             