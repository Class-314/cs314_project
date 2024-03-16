# cs314_project
Git Hub for CS314

For a better understanding of program read the following about the data storage structure.



Data Directory Structure that Stores Programs Data:
Data/
│
├── Reports/
│   ├── EFTDataReports/
│   │   ├─ProviderName-EFF.txt(Files related to EFT data report)
│   │   ├── ...(Additional EFT data report files)
│   │   └── ...
│   │
│   ├── MemberReports/
│   │   ├──MemberName_MMDDYYYY.txt (Files related to member report)
│   │   ├── ...(Additional member report files)
│   │   └── ...
│   │
│   ├── ProviderReports/
│   │   ├──ProviderName_MMDDYYYY.txt (Files related to provider report)
│   │   ├── ...(Additional provider report files)
│   │   └── ...
│   │
│   └── SummaryReports/
│       ├──MMDDYYYY.txt (File related to a summary report)
│       ├── ...(Additional summary report files)
│       └── ...
│
├── ServiceRecords/
│   ├── SR#MMDDYYYY.txt (File represents a service record, where MMDDYY represents the date of service)
│   ├── ...(Additional service record files)
│   └── ...
│
│
├── UserRecords/
│   │
│   ├── MemberRecords/
│   │   ├── M#########.txt (File represents a member's record, where #'s represent a member's 9-digit ID)
│   │   ├── ...(Additional member record files)
│   │   └── ...
│   │
│   └── ProviderRecords/
│       ├── P#########.txt (File represents a provider's record, where #'s represent a provider's 9-digit ID)
│       ├── ...(Additional provider record files)
│       └── ...
│
│
├── Register_IDs.txt (Text file containing registered IDs that have ever existed)
│
├── services.txt (File containing services present in the service directory)
│
└── SR_count.txt (Text file containing the count of service records generated)
