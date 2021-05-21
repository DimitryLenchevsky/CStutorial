import { LightningElement } from 'lwc';
import { ShowToastEvent } from 'lightning/platformShowToastEvent';
import CONTACT_OBJECT from '@salesforce/schema/Contact';
import NAME_FIELD from '@salesforce/schema/Contact.Name';
import ACCOUNT_FIELD from '@salesforce/schema/Contact.AccountId';
import ADDRESS_FIELD from '@salesforce/schema/Contact.MailingAddress';
import DESCRIPTION_FIELD from '@salesforce/schema/Contact.Description';
import PHONE_FIELD from '@salesforce/schema/Contact.Phone';
import MOBILE_FIELD from '@salesforce/schema/Contact.MobilePhone';

export default class TaskContactCreate extends LightningElement {
    isShowModal = false;

    objectApiName = CONTACT_OBJECT;
    fields = [NAME_FIELD, ACCOUNT_FIELD, PHONE_FIELD, MOBILE_FIELD, ADDRESS_FIELD, DESCRIPTION_FIELD];
    handleSuccess(event) {
        const toastEvent = new ShowToastEvent({
            title: "Contact is created",
            message: "Record ID: " + event.detail.id,
            variant: "success"
        });
        this.dispatchEvent(toastEvent);
    }

    showModalBox() {
        this.isShowModal = true;
    }

    hideModalBox() {
        this.isShowModal = false;
    }
}