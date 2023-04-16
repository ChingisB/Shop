import { TestBed } from '@angular/core/testing';

import { ApiConstService } from './api-const.service';

describe('ApiConstService', () => {
  let service: ApiConstService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ApiConstService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
