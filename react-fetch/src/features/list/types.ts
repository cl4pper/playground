import { ResponseT } from "../../types/response";

export interface Comment {
  postId: number;
  id: number;
  name: string;
  email: string;
  body: string;
}

export interface FetchResponse extends ResponseT {
  data?: Comment[] | null;
}
