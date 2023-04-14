import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NewCommentComponent } from './new-comment.component';

describe('NewcommentComponent', () => {
  let component: NewCommentComponent;
  let fixture: ComponentFixture<NewCommentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NewCommentComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NewCommentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
