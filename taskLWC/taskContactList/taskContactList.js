import { LightningElement, wire, track, api } from 'lwc';
import getContactsByAccount from '@salesforce/apex/lwcTaskData.retrieveContactList';
import { updateRecord } from 'lightning/uiRecordApi';
import { deleteRecord } from 'lightning/uiRecordApi';
import { refreshApex } from '@salesforce/apex';
import { ShowToastEvent } from 'lightning/platformShowToastEvent';

const COLUMNS = [
    { label: 'First Name', fieldName: 'FirstName', editable: true },
    { label: 'Last Name', fieldName: 'LastName', editable: true },
    { label: 'Address', fieldName: 'MailingStreet', editable: true },
    { label: 'Account', fieldName: 'Account_Naming__c',  editable: true }
];

export default class RelatedContactsByForAccount extends LightningElement {
    @track columns = COLUMNS;
    @track draftValues = [];
    @api recordId;
    @track recordsCount = 0;
    selectedRecords = [];

    @wire(getContactsByAccount)
    contacts;

    handleSave(event) {

        const recordInputs =  event.detail.draftValues.slice().map(draft => {
            const fields = Object.assign({}, draft);
            return { fields };
        });

        const promises = recordInputs.map(recordInput => updateRecord(recordInput));

        Promise.all(promises).then(records => {
            this.dispatchEvent(
                new ShowToastEvent({
                    title: 'Success',
                    message: 'Contact updated',
                    variant: 'success'
                })
            );
            this.draftValues = [];
            return refreshApex(this.contacts);
        }).catch(error => {
            this.dispatchEvent(
                new ShowToastEvent({
                    title: 'Error updating record',
                    message: error.body.message,
                    variant: 'error'
                })
            );
        });
    }

    getSelectedRecords(event) {
        const selectedRows = event.detail.selectedRows;
        this.recordsCount = event.detail.selectedRows.length;
        let conIds = new Set();

        for (let i = 0; i < selectedRows.length; i++) {
            conIds.add(selectedRows[i].Id);
        }
        this.selectedRecords = Array.from(conIds);
        if(this.recordsCount > 0){
            this.isDeleteButtonDisabled = false;
        }
        else{
            this.isDeleteButtonDisabled = true;
        }
    }

    deleteContacts(){
        if(this.selectedRecords){
            let promises = new Set();
            for(let i = 0; i < this.selectedRecords.length; i++){
                promises.add(deleteRecord(this.selectedRecords[i]));
            }

            Promise.all(promises).then(records =>{
                this.dispatchEvent(
                    new ShowToastEvent({
                        title: 'Success',
                        message: 'Contact deleted',
                        variant: 'success'
                    })
                );
                this.selectedRecords = [];
                this.isDeleteButtonDisabled = true;
                return refreshApex(this.contacts);
            }).catch(error => {
                this.dispatchEvent(
                    new ShowToastEvent({
                        title: 'Error deleting record',
                        message: error.body.message,
                        variant: 'error'
                    })
                );
            });
        }
    }
}