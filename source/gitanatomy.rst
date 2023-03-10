Anatomy of Git repositories
===========================

.. graphviz::

   digraph {
      node [ shape = component ]
      blob1 [ shape = note ]
      blob2 [ shape = note ]
      blob3 [ shape = note ]
      blob4 [ shape = note ]
      tree1 [ shape = folder ]
      tree2 [ shape = folder ]
      tree1 -> blob1
      tree1 -> blob2
      tree2 -> blob1
      tree1 -> blob3
      tree2 -> blob3
      tree2 -> blob4
      commit1 -> tree1
      commit2 -> tree2
      commit1 -> commit2
      commit2 -> commit3
      commit3 -> commit4
      commit5 -> commit6
      commit6 -> commit3
      head [ shape = point, xlabel = "HEAD", fontname = "monospace" ]
      head -> commit1
      branch1 [ shape = invhouse, label = "devel", fontname = "monospace" ]
      branch1 -> commit5
      branch2 [ shape = invhouse, label = "stable", fontname = "monospace" ]
      branch2 -> commit1
      tag1 [ shape = underline, label = "v1.0.0", fontname = "monospace" ]
      tag1 -> commit3
   }

+----------+----------+--------+
| Ref      | Tracking | Global |
+==========+==========+========+
| HEAD     | Yes      | No     |
+----------+----------+--------+
| tags     | No       | Yes/No |
+----------+----------+--------+
| branches | Yes      | No     |
+----------+----------+--------+
