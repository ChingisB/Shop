export interface Image{
    id: number,
    image: string,
    created_at: string,
    modified_at: string,
    deleted_at: string | null,
    product: number
}