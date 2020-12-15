(define (split-at lst n)
  (cond
    ((= n 0) (cons '() lst))
    ((null? (cdr lst)) (cons (cons (car lst) nil) nil))
    (else 
      (define rest (split-at (cdr lst) (- n 1)))
      (cons (cons (car lst) (car rest)) (cdr rest))))
)


(define (compose-all funcs)
  (if (null? funcs) 
    (lambda (x) x)
    (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x))))
)


(define (compose-all-better-way funcs)
  (lambda (x)
    (if (null? funcs) 
      x
      ((compose-all (cdr funcs)) ((car funcs) x))))
)