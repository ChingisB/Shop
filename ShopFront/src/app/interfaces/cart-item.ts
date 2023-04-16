import { Product } from "./product";

export interface CartItem{
    id: number,
    quantity: number,
    product: Product,
    created_at: string,
    modified_at: string,
    deleted_at: string | null
}