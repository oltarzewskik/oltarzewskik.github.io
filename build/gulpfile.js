const gulp = require('gulp');
const sass = require('gulp-sass');

"use strict";
gulp.task('sass', function () {
    gulp.src('sass/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('../assets/css/'));
})
