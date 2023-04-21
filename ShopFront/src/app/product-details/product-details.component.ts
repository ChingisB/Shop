import {Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {Product} from "../interfaces/product";
import {ProductService} from "../product.service";
import {CommentService} from "../comment.service";
import {CommentListComponent} from "../comment-list/comment-list.component";
import {ProductDetails} from "../interfaces/product-details";

@Component({
  selector: 'app-product-details',
  templateUrl: './product-details.component.html',
  styleUrls: ['./product-details.component.css']
})
export class ProductDetailsComponent implements OnInit{
  @ViewChild('commentInput') commentInput: ElementRef | undefined;
  product: ProductDetails = <ProductDetails>{};
  constructor(private route: ActivatedRoute, private productService: ProductService, private commentService : CommentService) {
  }
  ngOnInit() : void {
    const routeParams = this.route.snapshot.paramMap;
    const productIdFromRoute = Number(routeParams.get('productID'));

    this.productService.getProduct(productIdFromRoute).subscribe(product => {
      this.product = product
    })
  }

  reformatImage(imageURL: string): string{
    return imageURL.replace("92.47.4.210:59001","127.0.0.1")
  }

  submitComment(text: string){
    if(this.commentInput != undefined){
      this.commentService.createComment(this.product.id,text).subscribe(comment => {})
      this.commentInput.nativeElement.value = "";
    }else{
      alert("undefined")
    }
  }
}
