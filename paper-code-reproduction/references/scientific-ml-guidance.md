# Scientific ML Guidance

Apply the relevant sections for scientific ML, computational science, engineering, medical, and other domain-constrained papers.

## A. Units and semantic consistency

Always document:

- physical or semantic units when they exist,
- coordinate systems or indexing conventions,
- normalization and whether it is physical, statistical, or purely numerical,
- domain constants or known parameter ranges,
- any transformation needed to compare reproduced outputs with paper outputs.

If units or conventions are unstated, record the ambiguity explicitly. Do not silently mix incompatible units, component orders, scales, or coordinate frames.

## B. Data split risks

Scientific and biomedical datasets often leak through structure, repeated measurements, simulations, or subject-specific correlations.

Check for:

- same specimen, patient, subject, simulation family, or source case appearing in train and test,
- neighboring time windows split across sets,
- load cases, boundary conditions, or parameter sweeps split incorrectly,
- augmented or generated samples leaking the same original source,
- benchmark splits that differ from the paper.

## C. Output types

Different output types need different checks.

### Scalar or parameter regression

Track:

- MAE,
- RMSE,
- relative error,
- calibration or uncertainty if reported,
- parameter range and extrapolation behavior.

### Curves, trajectories, or sequences

Track:

- pointwise error,
- peak error,
- peak location error,
- area-under-curve or accumulated quantity when meaningful,
- monotonicity, periodicity, hysteresis, or trend fidelity when relevant.

### Fields, maps, meshes, images, or structured arrays

Track:

- nodewise, pixelwise, voxelwise, or elementwise error,
- qualitative pattern match,
- boundary or edge artifacts,
- conservation, symmetry, or constraint violations when relevant.

## D. Model families

### Data-driven surrogate models

Verify:

- input parameter ranges,
- interpolation vs extrapolation,
- whether geometry, context, or experimental condition variation is encoded,
- whether normalization preserves domain meaning.

### Physics-informed or equation-constrained models

Verify:

- residual terms,
- boundary and initial condition enforcement,
- collocation or sampling strategy,
- nondimensionalization,
- tradeoff weights between data loss and constraint loss.

### Inverse problems

Verify:

- identifiability,
- regularization,
- noise model,
- whether the inverse target is unique,
- whether multiple solutions can fit the same observation.

## E. Restricted or hard-to-access data

In medical, industrial, proprietary, or high-cost simulation tasks, be careful with:

- tiny sample sizes,
- heterogeneous acquisition or simulation protocols,
- subject-specific or case-specific preprocessing,
- ethics-restricted or proprietary datasets that are impossible to access,
- outputs that look numerically good but are implausible in the domain.

When exact reproduction is blocked, produce the best proxy implementation and explain why it is only proxy-level evidence.
