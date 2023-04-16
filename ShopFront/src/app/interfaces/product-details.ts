import { Category } from "./category";
import { Image } from "./image";
import { Inventory } from "./inventory";
import { Vendor } from "./vendor";

export interface ProductDetails{
    id: number,
    inventory: Inventory,
    discount: number | null,
    images: Image[],
    category: Category,
    vendor: Vendor,
    rating: number | null,
    is_liked: boolean,
    name: string,
    description: string,
    price: number,
    created_at: string,
    modified_at: string,
    deleted_at: string | null
}