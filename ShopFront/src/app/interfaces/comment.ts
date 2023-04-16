import { UserInfoBrief } from "./user-info-brief";

export interface Comment{
    id: number,
    user: UserInfoBrief,
    text: string
}