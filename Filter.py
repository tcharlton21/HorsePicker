import csv


race_info_headers = ['race_id', 'track', 'race_number', 'distance', 'surface', 'date_time', 'race_description', 'available_bets']
horse_headers = ["PP", "Name", "B", "B1Rk", "Diff", "B2Rk", "RTAD", "xSt4Jky", "B3", "B3Rk", "4#", "4#Rk", "R", "AgeLastOut", "AgeLastWork", "Bf", "BfRk", "Dt", "ML", "T", "Jockey", "Jky R", "Trainer", "S", "PRIME", "Prk", "Diff-Prime", "Form", "Late", "LateRk", "LateDiff", "2CallPos", "PctE", "PctERk", "4#Diff", "C-Pace", "C-PaceRk", "C-PaceDiff", "Improv", "I-Frac", "I-FracRk", "Par", "Comment", "E1", "E2", "V1", "V1Rk", "WoScore", "WoScoreRk", "FD", "Frk", "FP", "2CallLen", "PiDex", "BE2", "E2r", "E2d", "Clm", "WO", "PCR", "PCRRk", "V1 Diff", "Post Time", "Eq", "Wt", "Fig", "FigRk", "FigDiff", "PScore", "Rail", "hAge", "PrDiff", "PredScore", "PredScoreRk", "intGreatestTrainingGap", "wFig", "wFigRk", "wFigDiff", "AvgB", "AvgBRk", "AvgBDiff", "Q", "QRk", "QDiff", "Wb", "WbRk", "WbDiff", "Rb", "RbRk", "RbDiff", "hAgeDup", "hAgeRk", "hAgeDiff", "CR", "CRRk", "CRDiff", "PcLn", "PcLnRk", "PcLnDiff", "LTS", "WoScoreDup", "WoScoreRkDup", "WoScoreDiff", "jkyPct", "CDesX", "JRating", "JRatingRk", "JRatingDiff", "Sex", "pF1", "pF2", "TTime", "TTimeRk", "TTimeDiff", "Fit", "Cls", "ClsRk", "ClsDiff", "DblForm", "DblFormRk", "DblFormDiff", "Vi", "FSize", "TSRR", "TRRR", "DSRR", "DRRR", "AvgE1", "AvgeE1Rk", "AvgE1Diff", "SPace", "SPaceRk", "SPaceDiff", "RStr", "RStrRk", "RStrDiff", "AProb", "AProbRk", "AProbDiff", "CLRcs", "CLDys", "tWins", "tStarts", "PLBGap", "2fFigLast", "2fFigLastRk", "2fFigLastDiff", "DecelF", "Med", "Late1", "Late1Rk", "Late1Diff", "SfLR", "FPLen", "TkLO", "StsLyff", "StsMt", "StsLsx", "Sire", "Odds", "OFin", "Win", "Place", "Show", "EType", "EMut", "EType2", "EMut2", "xSprints", "xRoutes", "xField", "Fims4", "DistLast", "Dist2Bk", "StsTnr", "MLDup", "MLRk", "MLDiff", "Low", "Pal", "PalRk", "PalDiff", "TP", "TPRk", "TPDiff", "PctECP2", "PctECP2Rk", "Top", "Ownr", "PMI", "PMIRk", "PMIDiff", "CMI", "CMIRk", "CMIDiff", "OP", "OPRk", "OPDiff", "CRA", "FTR", "Purse", "STA", "STARk", "PFig", "PFigRk", "PFigDiff", "PctDirty", "TWMt", "TWMtRk", "TSMt", "TWYr", "TSYr", "RWMt", "RWMtRk", "RSMt", "RWYr", "RSYr", "RShape", "Pimp", "PimpRk", "CXN", "CXNRk", "Surf", "LyCt", "Rt1Ct", "T1Ct", "Consty", "ConstyRk", "ConstyDiff", "PRtg", "PRtgRk", "PRtgDiff", "AFR", "AFRRk", "Gap1", "Alcmy", "AlcmyRk", "Gap2", "CFA", "CFARk", "Gap3", "JPR", "JPRRk", "Gap4", "JPRClass", "JPRClassRk", "Gap5", "JMLPr", "JMLPrRk", "Gap6", "JMLF", "PED", "PEDRk", "Gap7", "QRt", "QRtRk", "Gap8", "UPR", "UPRRk", "Gap9", "UMLPr", "UMLPrRk", "Gap10", "CXNGap", "CmpdE1", "CmpdE1Rk", "Gap11", "CmpdE2", "CmpdE2Rk", "Gap12", "CmpdTT", "CmpdTTRk", "Gap13", "CmpdLate", "CmpdLateRk", "Gap14", "CmpdSP", "CmpdSPRk", "Gap15", "CmpdAP", "CmpdAPRk", "Gap16", "CmpdPctE", "CmpdPctERk", "Gap17", "P-Fit", "P-FitRk", "Gap18", "BestWFig", "BestWFigRk", "Gap19", "LtSlnt", "LtSlntRk", "Gap20", "CmpdPM", "CmpdPMRk", "Gap21", "UF1", "UF1Rk", "Gap22", "UF2", "UF2Rk", "Gap23", "UF3", "UF3Rk", "Gap24", "UF4", "UF4Rk", "Gap25", "UF5", "UF5Rk", "Gap26", "UF6", "UF6Rk", "Gap27", "UF7", "UF7Rk", "Gap28", "UF8", "UF8Rk", "Gap29", "Dam", "DamsSire", "SiresSire", "BCProb", "UPRProb", "Reserved1", "Reserved2", "Reserved3", "Reserved4", "Reserved5", "Reserved6", "Reserved7", "Reserved8", "Reserved9", "Reserved10", "Reserved11", "Reserved12", "FSP", "FSPRk", "FSPDiff", "FSF", "FSFRk", "FSFDiff", "W2W", "W2WRk", "W2WDiff", "HTye", "QDrive", "ClsCon", "ClsConRk", "ClsConDiff", "EaCon", "EaConRk", "EaConDiff", "FigCon", "FigConRk", "FigConDiff", "FmCon", "FmConRk", "FmConDiff", "LtCon", "LtConRk", "LtConDiff", "PwrCon", "PwrConRk", "PwrConDiff", "ESPShape", "HDWPScr", "HDWPScrRk", "HDWPScrDiff", "StyleHDW", "QAlt", "QAltRk", "QAltDiff", "Stge", "~"]
race_dict = {}
horse_dict = {}

with open("05-27-2016JCP.txt", "r") as csvfile:
    reader = csv.reader(csvfile)
    race_id = 0
    horseBool = False
    next(reader)
    for row in reader:
        # Check for end of race delimiter
        if row[0] == 'end_of_race.':
            race_id += 1
            horseBool = False
            continue
        # Skip the horse headers row
        if row[0] == 'PP':
            horseBool = True
            continue
        # Process race info
        if race_id not in race_dict and horseBool == False:
            # Split the row into a list of values
            values = row[0].split(' ')

            # Assign the values to variables, ignoring additional values
            track_name, race_number, distance, surface, date_time, *_ = values

            row = next(reader)
            race_description = row[0]
            row = next(reader)
            available_bets = row[0]
            race_dict[race_id] = {
                'race_id': race_id,
                'track': track_name,
                'race_number': race_number,
                'distance': distance,
                'surface': surface,
                'date_time': date_time,
                'race_description': race_description,
                'available_bets': available_bets
            }
            next(reader)
            next(reader)
            next(reader)
        # Process horse info
        if horseBool == True:
            if race_id not in horse_dict:
                horse_dict[race_id] = []
            horse_dict[race_id].append({k: v for k, v in zip(horse_headers, row)})

# Writing race information to a CSV file
with open('Race_info_5-27-2016.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=race_info_headers)
    writer.writeheader()  # write the headers
    for race_id, race_data in race_dict.items():
        race_data['race_id'] = race_id  # add the race_id to the row
        writer.writerow(race_data)  # write the data

# Writing horse information to a CSV file
with open('Horse_info_5-27-2016.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['race_id'] + horse_headers)# + race_info_headers)
    writer.writeheader()  # write the headers
    for race_id, horses in horse_dict.items():
        for horse in horses:
            horse['race_id'] = race_id  # add the race_id to the row
            writer.writerow(horse)  # write the data