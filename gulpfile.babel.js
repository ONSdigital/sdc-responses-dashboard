import gulp from "gulp";
import babel from "gulp-babel";
import cleanCSS from "gulp-clean-css";
import rename from "gulp-rename";
import del from "del";
import uglify from "gulp-uglify";


gulp.task("clean:dist", () => del(
    "app/static/dist/"
));

// transpile JS into ES5 for backwards compatibility
gulp.task("transpile:scripts", () => gulp.src("app/static/assets/js/*.js")
    .pipe(babel())
    .pipe(rename({
        suffix: ".min"
    }))
    .pipe(gulp.dest("app/static/dist/js")));

// minify JS files
gulp.task("minify:scripts", (done) => {
    gulp.src("app/static/dist/js/*.js")
        .pipe(uglify())
        .pipe(gulp.dest("app/static/dist/js/"));
    done();
});

// minify CSS files
gulp.task("minify:styles", (done) => {
    gulp.src("app/static/assets/css/*.css")
        .pipe(cleanCSS())
        .pipe(rename({
            suffix: ".min"
        }))
        .pipe(gulp.dest("app/static/dist/css/"));
    done();
});

gulp.task("compile", gulp.series("clean:dist", "transpile:scripts", gulp.parallel("minify:scripts", "minify:styles")));

gulp.task("default", gulp.series("compile"));
