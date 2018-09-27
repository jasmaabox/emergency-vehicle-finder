% Converts ground truth data to csv
writetable(gTruth.LabelData, "labels.csv")
writetable(cell2table(gTruth.DataSource.Source), 'img_paths.csv')