import { Component } from '@angular/core';
import { FormsModule} from "@angular/forms";

@Component({
  selector: 'app-profile-settings',
  templateUrl: './profile-settings.component.html',
  styleUrls: ['./profile-settings.component.css']
})
export class ProfileSettingsComponent {
  username: string="";
  email: string="";
  firstName: string="";
  lastName: string="";
  country: string="";
  city: string="";
  address: string="";
  postalCode: string="";
  telephone: string="";

  onSubmit() {
    // здесь вы можете использовать значения переменных
    console.log(this.username);
    console.log(this.email);
    console.log(this.firstName);
    console.log(this.lastName);
    console.log(this.country);
    console.log(this.city);
    console.log(this.address);
    console.log(this.postalCode);
    console.log(this.telephone);
  }

}
