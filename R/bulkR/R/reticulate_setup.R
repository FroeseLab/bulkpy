## Code taken from:
## https://rstudio.github.io/reticulate/articles/package.html
## Meant to delay loading of python environmnet so user can set the python environment

# python modules to use
scipy <- NULL
sparse <- NULL
numpy <- NULL
ad <- NULL
md <- NULL
bp <- NULL

#' delay load python environment
#' @import reticulate
.onLoad <- function(libname, pkgname) {
  # use superassignment to update global reference to scipy
  scipy <<- reticulate::import("scipy", delay_load = TRUE)
  sparse <<- reticulate::import("scipy.sparse", delay_load = TRUE)
  numpy <<- reticulate::import("numpy", delay_load = TRUE)
  ad <<- reticulate::import('anndata',delay_load = TRUE,convert = FALSE)
  md <<- reticulate::import('mudata',delay_load = TRUE)
  bp <<- reticulate::import('bulkpy',delay_load = TRUE)
}