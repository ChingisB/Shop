import { Category } from "./category";
import { Image } from "./image";
import { Inventory } from "./inventory";
import { Vendor } from "./vendor";

export interface Product{
    id: number,
    inventory: Inventory,
    discount: number | null,
    image: Image,
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