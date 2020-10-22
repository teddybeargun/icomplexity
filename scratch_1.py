dataset[['tgk.txt']].V3 = gsub('^ ', '', dataset[['tgk.txt']] . V3)
dataset[['xcl.txt']].V3 = gsub(
    'ADJ/GEN', 'ADJ;GEN', dataset[['xcl.txt']] . V3, fixed=T)
dataset[['xcl.txt']].V3 = gsub(
    'AJD', 'ADJ', dataset[['xcl.txt']] . V3, fixed=T)
dataset[['slv.txt']].V3 = gsub(
    'PCTP', 'PTCP', dataset[['slv.txt']] . V3, fixed=T)


dataset_n[['ady.txt']].V3 = gsub(
    'N;ERG;PL;DEF;DEF', 'N;INS;PL;DEF', dataset_n[['ady.txt']] . V3, fixed=T)
dataset_n[['ady.txt']].V3 = gsub(
    'N;ERG;PL;DEF;NDEF', 'N;INS;PL;NDEF', dataset_n[['ady.txt']] . V3, fixed=T)
dataset_n[['ady.txt']].V3 = gsub(
    'N;ERG;SG;DEF;DEF', 'N;INS;SG;DEF', dataset_n[['ady.txt']] . V3, fixed=T)
dataset_n[['ady.txt']].V3 = gsub(
    'N;ERG;SG;DEF;NDEF', 'N;INS;SG;NDEF', dataset_n[['ady.txt']] . V3, fixed=T)


dataset_n[['ces.txt']].V1 = ifelse(grepl(';ANIM;', dataset_n[['ces.txt']] . V3, fixed=T), paste0(
    dataset_n[['ces.txt']].V1, '-ANIM'), paste0(dataset_n[['ces.txt']] . V1))
dataset_n[['ces.txt']].V1 = ifelse(grepl(';INAN;', dataset_n[['ces.txt']] . V3, fixed=T), paste0(
    dataset_n[['ces.txt']].V1, '-INAN'), paste0(dataset_n[['ces.txt']] . V1))
dataset_n[['ces.txt']].V3 = gsub(
    ';ANIM;', ';', dataset_n[['ces.txt']] . V3, fixed=T)
dataset_n[['ces.txt']].V3 = gsub(
    ';INAN;', ';', dataset_n[['ces.txt']] . V3, fixed=T)


temp_anim = subset(dataset_n[['rus.txt']], set(V3) & set(
    make_tuple("N;ACC;ANIM;SG", "N;ACC;ANIM;PL")))
temp_anim = dataset_n[['rus.txt']][dataset_n[['rus.txt']] . set(V1) & set(unique(temp_anim . V1)),
temp_inan = subset(dataset_n[['rus.txt']], set(V3) & set(
    make_tuple("N;ACC;INAN;SG", "N;ACC;INAN;PL")))
temp_inan = dataset_n[['rus.txt']][dataset_n[['rus.txt']] . set(V1) & set(unique(temp_inan . V1)),
temp_other = dataset_n[['rus.txt']][~  (dataset_n[['rus.txt']] . set(V1) & set(unique(temp_inan . V1))),
                                    
                                    
temp_anim . V1 = paste0(temp_anim . V1, '-ANIM')
temp_anim = subset(temp_anim, ~  grepl(';INAN;', temp_anim . V3, fixed=T))
temp_anim . V3 = gsub(';ANIM;', ';', temp_anim . V3, fixed=T)
                                    
                                    
temp_inan . V1 = paste0(temp_inan . V1, '-INAN')
temp_inan = subset(temp_inan, ~  grepl(';ANIM;', temp_inan . V3, fixed=T))
temp_inan . V3 = gsub(';INAN;', ';', temp_inan . V3, fixed=T)
                                    
                                    
dataset_n[['rus.txt']] = rbind(temp_anim, temp_inan, temp_other)
dataset_n[['rus.txt']] = dataset_n[['rus.txt']][order(dataset_n[['rus.txt']] . V1),
