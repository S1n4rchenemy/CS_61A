;;;;;;;;;;;;;;;;
; Question 4.1 ;
;;;;;;;;;;;;;;;;

(define (factorial x) 
    (if (= x 1) 
        1
        (* x (factorial (- x 1)))))


;;;;;;;;;;;;;;;;
; Question 4.2 ;
;;;;;;;;;;;;;;;;

(define (fib n)
    (if (< n 2)
        n
        (+ (fib (- n 1)) (fib (- n 2)))))


;;;;;;;;;;;;;;;
; Quetion 5.1 ;
;;;;;;;;;;;;;;;

(define (my-append a b)
    (if (equal? (cdr a) nil)
        (cons (car a) b)
        (cons (car a) (my-append (cdr a) b))))


;;;;;;;;;;;;;;;;
; Question 5.2 ;
;;;;;;;;;;;;;;;;

(define s '(5 4 (1 2) 3 7))

(car (cdr (cdr (cdr s))))


;;;;;;;;;;;;;;;;
; Question 5.3 ;
;;;;;;;;;;;;;;;;

(define (duplicate lst) 
    (if (equal? (cdr lst) nil)
        (list (car lst) (car lst))
        (cons (car lst) (cons (car lst) (duplicate (cdr lst))))))


;;;;;;;;;;;;;;;;
; Question 5.4 ;
;;;;;;;;;;;;;;;;

(define (insert element lst index)
    (if (= index 0)
        (cons element lst)
        (cons (car lst) (insert element (cdr lst) (- index 1)))))