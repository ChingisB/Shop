import { User } from "./user";

export interface PaymentInfo{
    id: number,
    user: User,
    payment_info: string,
    provider: string,
    account_no: string,
    expiry: Date
}