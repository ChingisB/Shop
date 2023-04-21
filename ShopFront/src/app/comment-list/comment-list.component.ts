import {Component, Input} from '@angular/core';
import {CommentService} from "../comment.service";
import { Comment} from "../interfaces/comment";

@Component({
  selector: 'app-comment-list',
  templateUrl: './comment-list.component.html',
  styleUrls: ['./comment-list.component.css']
})
export class CommentListComponent {
  @Input() productId : number = 0

  commentList : Comment[]=[];

  constructor(private commentService: CommentService) { }

  ngOnInit(): void {
    this.commentService.getComments(this.productId).subscribe(comments => {
      this.commentList = comments
    })
  }

}
