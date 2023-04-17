import { CreateCartItem } from "./create_cart"
import { Product } from "./product"
import { User } from "./user"

export interface Payment{
    id: number | null,
    amount: number,
    provider: string,
    status: string,
    created_at: string | null,
    modified_at: string | null,
}

export interface CreateOrder{
    items: CreateCartItem[],
    payment: Payment
}

export interface Order{
    id: number,
    user: User,
    payment: Payment,
    items: Product[],
    total: number,
    created_at: string,
    modified_at: string
}