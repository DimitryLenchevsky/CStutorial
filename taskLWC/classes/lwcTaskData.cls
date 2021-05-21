public with sharing class lwcTaskData {
    @AuraEnabled(Cacheable=true)
    public static List<Equipment__c> retrieveEquipmentRecords(){
        return [
                SELECT Name,
                        Description__c,
                        Type__c,
                        Office_Name__c
                FROM Equipment__c
                WHERE Status__c != 'In Use'
        ];
    }

    @AuraEnabled(Cacheable=true)
    public static List<Contact> retrieveUsers(){
        return [
                SELECT Name,
                        Email,
                        Office_Name__c,
                        Title
                FROM Contact
                WHERE Employee_User__c != NULL
        ];
    }

    @AuraEnabled(Cacheable=true)
    public static List<Contact> retrieveContactList() {
        return [
                SELECT Id,
                        FirstName,
                        LastName,
                        MailingStreet,
                        Account_Naming__c
                FROM Contact
                WHERE Account_Naming__c != NULL
        ];
    }

    @AuraEnabled(Cacheable=true)
    public static List<Contact> getContactsByAccount(String accountId) {
        return [SELECT Id, FirstName, LastName, Title, Phone, Email FROM Contact];
    }

    @AuraEnabled(Cacheable=true)
    public static List<Contact> getRelatedContacts(Id accountId) {
        return [
                SELECT Name, Title, Email, Phone
                FROM Contact
                WHERE AccountId = :accountId
                WITH SECURITY_ENFORCED
        ];
    }

    @AuraEnabled(cacheable=true)
    public static List<Account> getAccounts() {
        return [
                SELECT Name, AnnualRevenue, Industry
                FROM Account
                WITH SECURITY_ENFORCED
                ORDER BY Name
        ];
    }
}