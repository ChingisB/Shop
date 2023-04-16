export interface CreateCart{
    cart: CreateCartItem[]
}

export interface CreateCartItem{
    product_id: number,
    quantity: number
}