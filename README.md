# HP-iLO
iLO 4  HP ProLiant

```
{
 "in_post": 0,
 "log_drive_arrays": [
  {
   "status": "OP_STATUS_DEGRADED",
   "encr_self_stat": "OP_STATUS_OK",
   "name": "Controller on System Board",
   "has_accel": 1,
   "logical_drives": [
    {
     "status": "OP_STATUS_OK",
     "log_status": "LOG_OK",
     "lu_cache_flag": "LOG_CACHE_FLAG_NONMEMBER",
     "capacity": "279 GB",
     "name": "Logical Drive 01",
     "flt_tol": "RAID 1/RAID 1+0",
     "lu_cache_LUN": "HIDDEN",
     "encr_stat": "ENCR_NOT_ENCR",
     "physical_drives": [
      {
       "status": "OP_STATUS_OK",
       "encr_stat": "ENCR_NOT_ENCR",
       "drive_type": "PHY_ARRAY",
       "capacity": "279 GB",
       "name": "Physical Drive in Port 1I Box 1 Bay 1",
       "phys_status": "PHYS_OK",
       "model": "EG0300FCSPH",
       "serial_no": "44G0A0ERFTM91416",
       "fw_version": "HPD0",
       "location": "Port 1I Box 1 Bay 1"
      },
      {
       "status": "OP_STATUS_OK",
       "encr_stat": "ENCR_NOT_ENCR",
       "drive_type": "PHY_ARRAY",
       "capacity": "279 GB",
       "name": "Physical Drive in Port 1I Box 1 Bay 2",
       "phys_status": "PHYS_OK",
       "model": "EG0300FCSPH",
       "serial_no": "44F0A0XLFTM91416",
       "fw_version": "HPD0",
       "location": "Port 1I Box 1 Bay 2"
      }
     ]
    }
   ],
   "serial_no": "PDNLH0BRH7K1ID",
   "fw_version": "1.18",
   "accel_serial": "PDNLH0BRH7K1ID",
   "enclosures": [
    {
     "status": "OP_STATUS_OK",
     "name": "Drive Enclosure Port 1I Box 1",
     "ports": "4"
    },
    {
     "status": "OP_STATUS_OK",
     "name": "Drive Enclosure Port 2I Box 0",
     "ports": "4"
    }
   ],
   "hw_status": "OP_STATUS_OK",
   "encr_stat": "ENCR_NOT_ENABLED",
   "accel_cond": "OP_STATUS_DEGRADED",
   "model": "HP Smart Array P440ar Controller",
   "accel_tot_mem": "2097152 KB",
   "has_encrypt": 1,
   "encr_csp_stat": "OP_STATUS_OK"
  }
 ],
 "has_sa": 1,
 "hostpwr_state": "ON"
}
```