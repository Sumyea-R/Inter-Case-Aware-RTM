
case_id_col = {}
activity_col = {}
timestamp_col = {}
label_col = {}
pos_label = {}
neg_label = {}
dynamic_cat_cols = {}
static_cat_cols = {}
dynamic_num_cols = {}
static_num_cols = {}
filename = {}


#### Traffic fines settings ####
dataset = "traffic_fines"

filename[dataset] = "logdata/traffic_fines.csv"

case_id_col[dataset] = "Case ID"
activity_col[dataset] = "Activity"
timestamp_col[dataset] = "Complete Timestamp"
label_col[dataset] = "remtime"
pos_label[dataset] = "deviant"
neg_label[dataset] = "regular"

# features for classifier
dynamic_cat_cols[dataset] = ["Resource", "lastSent", "notificationType", "dismissal"]
static_cat_cols[dataset] = ["article", "vehicleClass"]
dynamic_num_cols[dataset] = ["expense", "duration", "month", "weekday", "hour"]
static_num_cols[dataset] = ["amount", "points"]



#### bpic2020 log settings ####
dataset = "bpic2020"

filename[dataset] = "logdata/bpic2020.csv"

case_id_col[dataset] = "Case ID"
activity_col[dataset] = "Activity"
timestamp_col[dataset] = "Complete Timestamp"
label_col[dataset] = "remtime"
pos_label[dataset] = "regular"
neg_label[dataset] = "deviant"

# features for classifier
dynamic_cat_cols[dataset] = ["Resource","Role", "month", "weekday", "hour"]
static_cat_cols[dataset] = []
dynamic_num_cols[dataset] = [ "duration","elapsed" ]
static_num_cols[dataset] = ["Amount"]

#### production log settings ####
dataset = "production"

filename[dataset] = "logdata/production.csv"

case_id_col[dataset] = "Case ID"
activity_col[dataset] = "Activity"
timestamp_col[dataset] = "Complete Timestamp"
label_col[dataset] = "remtime"
pos_label[dataset] = "regular"
neg_label[dataset] = "deviant"

# features for classifier
dynamic_cat_cols[dataset] = ["Activity", "Resource", "Report Type", "Worker ID","weekday"]
static_cat_cols[dataset] = ["Part Desc"]
dynamic_num_cols[dataset] = ["Qty Completed", "Qty for MRB", "activity_duration", "hour", "timesincelastevent", "timesincecasestart", "event_nr", "open_cases"]
static_num_cols[dataset] = ["Work Order Qty"]

